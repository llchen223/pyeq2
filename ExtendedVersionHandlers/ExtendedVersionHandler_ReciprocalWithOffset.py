from __future__ import print_function # prepare for conversion to Python 3
from __future__ import unicode_literals # prepare for conversion to Python 3
from __future__ import absolute_import # prepare for conversion to Python 3

#    pyeq2 is a collection of equations expressed as Python classes
#
#    Copyright (C) 2012 James R. Phillips
#    2548 Vera Cruz Drive
#    Birmingham, AL 35235 USA
#
#    email: zunzun@zunzun.com
#    web: http://zunzun.com
#
#    License: BSD-style (see LICENSE.txt in main source directory)

import pyeq2
from . import IExtendedVersionHandler


class ExtendedVersionHandler_ReciprocalWithOffset(IExtendedVersionHandler.IExtendedVersionHandler):
    
    def AssembleDisplayHTML(self, inModel):
        return inModel._HTML + '<br>' + inModel._leftSideHTML + ' = 1.0 / ' + inModel._leftSideHTML + ' + Offset'


    def AssembleDisplayName(self, inModel):
        return 'Reciprocal ' + inModel._baseName + ' With Offset'


    def AssembleSourceCodeName(self, inModel):
        return inModel.__class__.__name__ + "_ReciprocalWithOffset"


    def AssembleCoefficientDesignators(self, inModel):
        return inModel._coefficientDesignators + ['Offset']


    # overridden from abstract parent class
    def AppendAdditionalCoefficientBounds(self, inModel):
        if inModel.upperCoefficientBounds != []:
            inModel.upperCoefficientBounds.append(None)
        if inModel.lowerCoefficientBounds != []:
            inModel.lowerCoefficientBounds.append(None)


    def AssembleOutputSourceCodeCPP(self, inModel):
        return inModel.SpecificCodeCPP() + "\ttemp = 1.0 / temp + Offset;\n"


    # overridden from abstract parent class
    def GetAdditionalDataCacheFunctions(self, inModel, inDataCacheFunctions):
        return inDataCacheFunctions


    def GetAdditionalModelPredictions(self, inBaseModelCalculation, inCoeffs, inDataCacheDictionary, inModel):
        return self.ConvertInfAndNanToLargeNumber(1.0 / inBaseModelCalculation + inCoeffs[len(inCoeffs)-1])

