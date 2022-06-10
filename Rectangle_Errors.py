class RectangleError(Exception):
    RECT_TYPE_ERR = "Operation requires two Rectangle objects"
    RECT_ZERODIV_ERR = "Division requires RHS have non-zero dimensions"


def __init__(self, dscr_string=""):
    if not isinstance(dscr_string, str):
        dscr_string = str(dscr_string)
    super().__init__(dscr_string)
    self.description = dscr_string


def __str__(self):
    ret_str = "RectangleError: " + self.description
    return ret_str


# client (as a function) -----------------------------------
def main():
    r_1 = Rectangle("A", 3, 4)
    r_2 = Rectangle("B", 5, 2)

    r_1.show_me("r_1 is:")
    r_2.show_me("r_2 is:")
    print()

    r_3 = r_1 + r_2
    r_3.show_me("r_3 is:")

    r_4 = r_2 - r_1
    r_4.show_me("r_4 is:")
    print()

    (r_3 + r_4).show_me("r_3 + r_4 is:")
    (r_1 * r_3).show_me("r_1 * r_4 is:")
    (~r_1).show_me("~r_1 is:")

    # error testing
    print("Start error testing -----------\n")
    r_1 = Rectangle("A", 3, 4)
    r_1.show_me("r_1 is:")
    print()

    try:
        r_2 = r_1 + 3
        r_1.show_me("r_1 is:")
        print()
        r_2.show_me("r_2 is:")
        print()
    except RectangleError as err:
        print(type(err), ":", err)

    print()

    try:
        r_2 = r_1 / Rectangle("healthy", 4, 5)
        r_2.show_me("r_2 is:")
        print()
        r_2 = r_1 / Rectangle("skinny", 0, 43)
        r_2.show_me("r_2 is:")
        print()
    except RectangleError as err:
        print(type(err), ":", err)
        print()

    try:
        r_2 = r_1 / 4
        r_2.show_me("r_2 is:")
        print()
    except RectangleError as err:
        print(type(err), ":", err)
        print()


# END CLIENT main()  -------------------------------------------
# BEGIN CLASS Rectangle -------------------------------------------
class Rectangle:
    """ example of class and static methods/functions """

    # class ("static") intended constants
    ORIGINAL_DEFAULT_DIMENSION = 0.
    ORIGINAL_DEFAULT_LABEL = "(no label)"
    MIN_DIM = 0.
    MAX_DIM = 1000000.
    MIN_STRING_LENGTH = 1

    # class attributes that will change over time
    default_dimension = ORIGINAL_DEFAULT_DIMENSION
    default_label = ORIGINAL_DEFAULT_LABEL

    # initializer ("constructor") method -------------------------------
    def __init__(self,
                 label=None,
                 width=None,
                 height=None):

        # repair mutable defaults
        if (width == None):
            width = self.default_dimension
        if (height == None):
            height = self.default_dimension
        if (label == None):
            label = self.default_dimension

        # instance attributes
        if (not self.set_width(width)):
            self.width = self.default_dimension
        if (not self.set_height(height)):
            self.height = self.default_dimension
        if (not self.set_label(label)):
            self.label = self.default_label

    # mutators -----------------------------------------------
    def set_width(self, width):
        if not self.valid_dimension(width):
            return False
        # else
        self.width = width
        return True

    def set_height(self, height):
        if not self.valid_dimension(height):
            return False
        # else
        self.height = height
        return True

    def set_width_height(self, width, height):
        if not (self.valid_dimension(width)
                and
                self.valid_dimension(height)):
            return False
        # else
        self.width = width
        self.height = height
        return True

    def set_label(self, label):
        if not self.valid_string(label):
            return False
        # else
        self.label = label
        return True

    # accessors -----------------------------------------------
    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_label(self):
        return self.label

    def get_area(self):
        return self.width * self.height

    def get_perimiter(self):
        return 2 * (self.width + self.height)

    # output methods  ----------------------------------------
    def show_me(self, client_intro_str="RECTANGLE DATA:"):
        print(str(client_intro_str) + str(self))

    # static and class helpers -------------------------------
    @classmethod
    def valid_dimension(cls, dim_to_test):
        if (
                (type(dim_to_test) != float and type(dim_to_test) != int)
                or
                not (cls.MIN_DIM <= dim_to_test <= cls.MAX_DIM)
        ):
            return False
        # else
        return True

    @classmethod
    def valid_string(cls, string_to_test):
        if (type(string_to_test) != str
                or
                len(string_to_test) < cls.MIN_STRING_LENGTH):
            return False
        # else
        return True

    @staticmethod
    def which_is_bigger_ref(rect_1, rect_2):
        if (rect_1.get_area() > rect_2.get_area()):
            return rect_1
        else:
            return rect_2

    @classmethod
    def which_is_bigger_clone(cls, rect_1, rect_2):
        if (rect_1.get_area() > rect_2.get_area()):
            larger_ref = rect_1
        else:
            larger_ref = rect_2
        ret_obj = cls(larger_ref.label,
                      larger_ref.width, larger_ref.height)
        return ret_obj

    # class mutators and accessors ----------------------------
    @classmethod
    def set_default_dim(cls, new_dimension):
        if not cls.valid_dimension(new_dimension):
            return False
        # else
        cls.default_dimension = new_dimension
        return True

    @classmethod
    def set_default_lab(cls, new_label):
        if not cls.valid_string(new_label):
            return False
        # else
        cls.default_label = new_label
        return True

    @classmethod
    def get_default_dim(cls):
        return cls.default_dimension

    @classmethod
    def get_default_lab(cls):
        return cls.default_label

    # special function and operator overrides  ---------------
    def __str__(self):
        ret_str = (("\n    label: {}"
                    + "\n    dimensions: {}(w) x {}(h).").
                   format(self.label, self.width, self.height))
        return ret_str

    def __add__(self, other):
        if not isinstance(other, Rectangle):
            raise RectangleError(RectangleError.RECT_TYPE_ERR)
        new_label = "(" + self.label + " + " + other.label + ")"
        new_width, new_height \
            = self.width + other.width, self.height + other.height
        ret_rect = Rectangle(new_label, new_width, new_height)
        return ret_rect

    def __sub__(self, other):
        if not isinstance(other, Rectangle):
            raise RectangleError(RectangleError.RECT_TYPE_ERR)
        new_label = "(" + self.label + " - " + other.label + ")"
        new_width, new_height \
            = self.width - other.width, self.height - other.height
        ret_rect = Rectangle(new_label, new_width, new_height)
        return ret_rect

    def __mul__(self, other):
        if not isinstance(other, Rectangle):
            raise RectangleError(RectangleError.RECT_TYPE_ERR)
        new_label = "(" + self.label + " * " + other.label + ")"
        new_width, new_height \
            = self.width * other.width, self.height * other.height
        ret_rect = Rectangle(new_label, new_width, new_height)
        return ret_rect

    def __truediv__(self, other):
        if not isinstance(other, Rectangle):
            raise RectangleError(RectangleError.RECT_TYPE_ERR)

        if (other.width == 0 or other.height == 0):
            raise RectangleError(RectangleError.RECT_ZERODIV_ERR)
        new_label = "(" + self.label + " / " + other.label + ")"
        new_width, new_height \
            = self.width / other.width, self.height / other.height
        ret_rect = Rectangle(new_label, new_width, new_height)
        return ret_rect

    def __invert__(self):
        """ ~ operator exchanges width and height """
        new_label = "(~" + self.label + ")"
        new_width, new_height \
            = self.height, self.width
        ret_rect = Rectangle(new_label, new_width, new_height)
        return ret_rect


# END CLASS Rectangle -------------------------------------------
# -------------- main program -------------------
if __name__ == "__main__":
    main()