##Import entire Module(Eccomemce)
#Remember that a Module is to be used in a completely different file 
import  ecommerce.shipping


ecommerce.shipping.calc_shipping()


##Method Two
##Better than first

##Import Package--->MODULE--->THEN Functions
from ecommerce.shipping import calc_shipping


calc_shipping()
calc_shipping()
calc_shipping()


##Method 3

from ecommerce import shipping

shipping.calc_shipping()
shipping.calc_shipping()
