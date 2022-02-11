class Gaussian_Integer():
    ''' represents a bank account you can deposit and withdraw from'''
    def __init__(self,real_number,imaginary_number):
        self.real = real_number
        self.imaginary = imaginary_number
    
    def __str__(self):
        return str(self.real) + "+" + str(self.imaginary) + "i"

    def multiply(self,gaussian_number):
        real_number = (self.real * gaussian_number.real) - (self.imaginary * gaussian_number.imaginary)
        imaginary_number = (self.real * gaussian_number.imaginary) + (self.imaginary * gaussian_number.real)
        return Gaussian_Integer(real_number, imaginary_number)
    
    def add (self, gaussian_number):
        real_number = self.real + gaussian_number.real
        imaginary_number =  self.imaginary + gaussian_number.imaginary
        return Gaussian_Integer(real_number, imaginary_number)


if __name__ == '__main__':
    u = Gaussian_Integer(1,1)
    v = Gaussian_Integer(1,2)
    w = u.multiply(u)
    x = u.add(v).add(w)
    print(u)
    print(v)
    print(w)
    print(x)

    a = Gaussian_Integer(1,2)
    b = Gaussian_Integer(2,3)
    c = a.multiply(b)
    print(c)

    
