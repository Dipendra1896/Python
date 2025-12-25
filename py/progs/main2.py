from sys import path
path.append('../packages')

import extra.iota
print(extra.iota.FunI())
  

 #Can be also written as
from sys import path
path.append('../packages')

from extra.iota import FunI
print(FunI())



# Accessing sigma and tau modules
from sys import path

path.append('../packages')

import extra.good.best.sigma
from extra.good.best.tau import FunT

print(extra.good.best.sigma.FunS())
print(FunT())

#You can make your life easier by using aliasing:

from sys import path

path.append("../packages")

import extra.good.best.sigma as sig
import extra.good.alpha as alp

print(sig.FunS())
print(alp.FunA())



from sys import path

path.append('../packages/extrapack.zip')

import extra.good.best.sigma as sig
import extra.good.alpha as alp
from extra.iota import FunI
from extra.good.beta import FunB

print(sig.FunS())
print(alp.FunA())
print(FunI())
print(FunB())




