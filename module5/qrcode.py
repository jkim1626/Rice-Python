"""
QR Code Generator
"""

import comp140_module5 as qrcode
import comp140_module5_z256 as z256

def divide_terms(coefficient1, power1, coefficient2, power2):
    """
    Computes the quotient of two terms.

    The degree of the first term, power1, must be greater than or
    equal to the degree of the second term, power2.

    Inputs:
        - coefficient1: a Z_256 number representing the coefficient of the first polynomial term
        - power1: an integer representing the power of the first term.
        - coefficient2: a Z_256 number representing the coefficient of the second polynomial term
        - power2: an integer representing the power of the second term.

    Returns: an instance of a Polynomial that is the resulting
    term.
    """
    # From recipe: (a*x^b) / (c*x^d) = (a/c) * x^(b-d)
    new_coeff = z256.div(coefficient1, coefficient2)
    new_pow = power1 - power2

    # Represent our answer as a Polynomial
    divided = Polynomial()
    divided = divided.add_term(new_coeff, new_pow)
    return divided

class Polynomial:
    """
    A class used to abstract methods on a polynomial in the finite
    field Z_256 (including numbers from 0 through 255).

    Since 256 is not prime, but is rather of the form p^n = 2^8, this
    representation uses special arithmetic via the z256 module so as to
    preserve multiplicative inverses (division) inside this field.
    """

    def __init__(self, terms=None):
        """
        Creates a new Polynomial object.  If a dictionary of terms is provided,
        they will be the terms of the polynomial,
        otherwise the polynomial will be the 0 polynomial.

        inputs:
            - terms: a dictionary of terms mapping powers to coefficients or None
              (None indicates that all coefficients are 0)
        """
        if terms != None:
            self._terms = dict(terms)
        else:
            self._terms = {}

    def __str__(self):
        """
        Returns: a string representation of the polynomial, containing the
        class name and all of the terms.
        """
        # Create a string of the form "ax^n + bx^n-1 + ... + c" by
        # creating a string representation of each term, and inserting
        # " + " in between each
        term_strings = []

        # Add the highest powers first
        powers = list(self._terms.keys())
        powers.sort(reverse=True)
        for power in powers:
            coefficient = self._terms[power]
            # Don't print out terms with a zero coefficient
            if coefficient != 0:
                # Don't print "x^0"; that just means it's a constant
                if power == 0:
                    term_strings.append("%d" % coefficient)
                else:
                    term_strings.append("%d*x^%d" % (coefficient, power))

        terms_str = " + ".join(term_strings)
        if terms_str == "":
            terms_str = "0"
        return "Polynomial: %s" % terms_str

    def __eq__(self, other_polynomial):
        """
        Check if another polynomial is equvalent

        inputs:
            - other_polynomial: a Polynomial object

        Returns a boolean: True if other_polynomial contains
        the same terms as self, False otherwise.
        """
        # Make sure that other_polynomial is a Polynomial
        if not isinstance(other_polynomial, Polynomial):
            return False

        # Get the terms of the other_polynomial
        terms = other_polynomial.get_terms()

        # Check that all terms in other_polynomial appear in self
        for power, coefficient in terms.items():
            if coefficient != 0:
                if power not in self._terms:
                    return False
                if self._terms[power] != coefficient:
                    return False

        # Check that all terms in self appear in other_polynomial
        for power, coefficient in self._terms.items():
            if coefficient != 0:
                if power not in terms:
                    return False
                if terms[power] != coefficient:
                    return False

        return True

    def __ne__(self, other_polynomial):
        """
        Check if another polynomial is NOT equivalent

        inputs:
            - other_polynomial: a Polynomial object

        Return a boolean: False if other_polynomial contains the same terms
        as self, True otherwise.
        """
        return not self.__eq__(other_polynomial)

    def get_terms(self):
        """
        Returns: a dictionary of terms, mapping powers to coefficients.
        This dictionary is a completely new object and is not a reference
        to any internal structures.
        """
        terms = dict(self._terms)
        return terms

    def get_degree(self):
        """
        Returns: the maximum power over all terms in this polynomial.
        """
        # Since we don't clean zero-coefficient powers out of our dictionary,
        # we need a trickier get_degree function, to take into account that
        # some coefficients could be zero.
        highest_power = 0
        for power in self._terms:
            if (power > highest_power) and (self._terms[power] != 0):
                highest_power = power

        return highest_power


    def get_coefficient(self, power):
        """
        Determines the coefficient of x^(power) in this polynomial.
        If there is no coefficient of x^(power), this method
        returns 0.

        inputs:
            - power: an integer representing a polynomial power

        Returns: a Z_256 number that is the coefficient or 0 if there
                 is no term of the given power
        """
        if power in self._terms:
            return self._terms[power]
        else:
            return 0

    def add_term(self, coefficient, power):
        """
        Add one term to this polynomial.

        inputs:
            - coefficient: a Z_256 number representing the coefficient of the term
            - power: an integer representing the power of the term

        Returns: a new Polynomial that is the sum of adding this polynomial
        to (coefficient) * x^(power) using Z_256 arithmetic to add
        coefficients, if necessary.
        """
        #self as dictionary to allow iteration
        terms = self.get_terms()
        
        if power in terms:
            terms[power] = z256.add(terms[power], coefficient)
        else:
            terms[power] = coefficient
            
        return Polynomial(terms)

    def subtract_term(self, coefficient, power):
        """
        Subtract one term from this polynomial.

        inputs:
            - coefficient: a Z_256 number representing the coefficient of the term
            - power: an integer representing the power of the term

        Returns: a new Polynomial that is the difference of this polynomial
        and (coefficient) * x^(power) using Z_256 arithmetic to subtract
        coefficients, if necessary.
        """
        #addition and subtraction the same in Z256
        terms = self.add_term(coefficient, power)
        
        return terms

    def multiply_by_term(self, coefficient, power):
        """
        Multiply this polynomial by one term.

        inputs:
            - coefficient: a Z_256 number representing the coefficient of the term
            - power: an integer representing the power of the term

        Returns: a new Polynomial that is the product of multiplying
        this polynomial by (coefficient) * x^(power).
        """
        #self as dictionary to allow iteration
        original_terms = self.get_terms()
        product = {}
        
        for original_power in original_terms:
            
            #multiply each portion 
            new_power = original_power + power
            new_coef = z256.mul(original_terms[original_power], coefficient)
            
            #add product to product terms
            product[new_power] = new_coef
        
        return Polynomial(product)

    def add_polynomial(self, other_polynomial):
        """
        Compute the sum of the current polynomial other_polynomial.

        inputs:
            - other_polynomial: a Polynomial object

        Returns: a new Polynomial that is the sum of both polynomials.
        """
        #copy of self
        poly_sum = Polynomial(self.get_terms())
        
        #other_terms as dictionary to allow iteration
        other_terms = other_polynomial.get_terms()
        for other_power in other_terms:
            
            #add each term
            poly_sum = poly_sum.add_term(other_terms[other_power],other_power)

        return poly_sum

    def subtract_polynomial(self, other_polynomial):
        """
        Compute the difference of the current polynomial and other_polynomial.

        inputs:
            - other_polynomial: a Polynomial object

        Returns: a new Polynomial that is the difference of both polynomials.
        """
        #addition and subtraction the same in Z256
        return self.add_polynomial(other_polynomial)

    def multiply_by_polynomial(self, other_polynomial):
        """
        Compute the product of the current polynomial and other_polynomial.

        inputs:
            - other_polynomial: a Polynomial object

        Returns: a new Polynomial that is the product of both polynomials.
        """
        #copy of self
        poly = Polynomial(self.get_terms())
       
        poly_product = Polynomial()
        
        #other_terms as dictionary to allow iteration
        other_terms = other_polynomial.get_terms()
        
        for other_power in other_terms:
            #multiplication term by term
            poly_parts = poly.multiply_by_term(other_terms[other_power],other_power)
            poly_product = poly_product.add_polynomial(poly_parts)
        
        return poly_product

    def remainder(self, denominator):
        """
        Compute a new Polynomial that is the remainder after dividing this
        polynomial by denominator.

        Note: does *not* return the quotient; only the remainder!

        inputs:
            - denominator: a Polynomial object

        Returns: a new polynomial that is the remainder
        """
        #og_poly as dictionary to allow iteration
        og_poly = self.get_terms()
        
        #copy of poly_remainder
        poly_remainder = Polynomial(self.get_terms())
        
        poly_remainder_degree = poly_remainder.get_degree()
        denominator_terms = denominator.get_terms()
        denominator_degree = denominator.get_degree()
        
        #edge case where numerator and denominator are the same, 
        #thus remainder should be zero
        if Polynomial(og_poly) == denominator:
            return Polynomial()
        
        #polynomial long division
        while poly_remainder.get_degree() >= denominator_degree:
            poly_remainder_terms = poly_remainder.get_terms()
            quotient_part = divide_terms(poly_remainder_terms[poly_remainder_degree],
                                         poly_remainder_degree,
                                         denominator_terms[denominator_degree],
                                         denominator_degree)
                
            mid_polynomial = denominator.multiply_by_polynomial(quotient_part)
                
            poly_remainder = poly_remainder.subtract_polynomial(mid_polynomial)
            poly_remainder_degree = poly_remainder.get_degree()
            
            #edge case where numerator is divisable by denominator
            #thus remainder should be zero
            if poly_remainder == Polynomial():
                return poly_remainder

        return poly_remainder

def create_message_polynomial(message, num_correction_bytes):
    """
    Creates the appropriate Polynomial to represent the
    given message. Relies on the number of error correction
    bytes (k). The message polynomial is of the form
    message[i]*x^(n+k-i-1) for each number/byte in the message.

    Inputs:
        - message: a list of integers (each between 0-255) representing data
        - num_correction_bytes: an integer representing the number of
          error correction bytes to use

    Returns: a Polynomial with the appropriate terms to represent the
    message with the specified level of error correction.
    """
    message_poly = Polynomial()
    for num in range(len(message)):
        #attributes of each new term
        coef = message[num]
        power = len(message) + num_correction_bytes - num - 1
        
        #add to whole message_poly
        message_poly = message_poly.add_term(coef,power)
    
    return message_poly

def create_generator_polynomial(num_correction_bytes):
    """
    Generates a static generator Polynomial for error
    correction, which is the product of (x-2^i) for all i in the
    set {0, 1, ..., num_correction_bytes - 1}.

    Inputs:
        - num_correction_bytes: desired number of error correction bytes.
                                In the formula, this is represented as k.

    Returns: generator Polynomial for generating Reed-Solomon encoding data.
    """
    generator_poly = Polynomial({0:1})
    for num in range(num_correction_bytes):
        #attributes of each new term
        term = Polynomial({1:1})
        term = term.subtract_term(z256.power(2,num),0)
        
        #mulitply to whole generator_poly
        generator_poly = generator_poly.multiply_by_polynomial(term)
    
    return generator_poly

def reed_solomon_correction(encoded_data, num_correction_bytes):
    """
    Corrects the encoded data using Reed-Solomon error correction

    Inputs:
        - encoded_data: a list of integers (each between 0-255)
                        representing an encoded QR message.
        - num_correction_bytes: desired number of error correction bytes.

    Returns: a polynomial that represents the Reed-Solomon error
    correction code for the input data.
    """
    numerator = create_message_polynomial(encoded_data, num_correction_bytes)
    denominator = create_generator_polynomial(num_correction_bytes)
    
    return numerator.remainder(denominator)


# Uncomment the following line when you are ready to generate an
# actual QR code.  To do so, you must enter a short message in the
# "info" text box and hit return (be sure to hit return!).  You then
# must push the "Generate!" button.  This will generate a QR code for
# you to view - try scanning it with your phone!  If you would like to
# save your QR codes, you can use the "Image in a New Window" button
# to create a .png file that you can save by right clicking in your
# browser window.

qrcode.start(reed_solomon_correction)