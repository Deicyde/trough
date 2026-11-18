# Units

The folder [Physlib/Units/](https://github.com/leanprover-community/physlib/tree/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units): 16 modules, an article each, in path order with Basic.lean first in its folder; then 1 folder below it, a page each, 23 modules in all.

The repository's API map for this folder, *Units* ([Physlib/Units/API-map.md](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/API-map.md)): its Content section, with the sentences it marks as not yet formalized left out (…). A citation \[n\] links the module its n-th Lean reference names.

*Content (Alpha)*

> ### Dimensions
>
> A dimension assigns a rational exponent to each base dimension, and two dimensions with the same exponents are equal. [\[1\]](dimension.md) Dimensions form a commutative group with a rational power operation. [\[2\]](dimension.md) The exponents of a product, of the unit, of an inverse, of a quotient and of a natural power follow from the exponents of the factors. [\[3\]](dimension.md) Each base dimension has its base vector, whose exponents are one at that base dimension and zero elsewhere. [\[4\]](dimension.md) The vocabulary of base quantity, derived quantity and quantity dimension is that of ISO/IEC 80000-1 \{1} and of the International vocabulary of metrology \{2}. The design of this API is discussed on the Lean Zulip \{3}.
>
> A change of base-dimension set is a monoid homomorphism of dimensions, either an injective embedding of one set into another or a surjective reduction of a richer set onto a coarser one, so a relabelling that does not preserve products, inverses and rational powers is not expressible. [\[5\]](dimension.md)
>
> ### The LTMCT and ISQ base sets
>
> The LTMCT set has five base dimensions, length, time, mass, charge and temperature, whose initials give the name, each with its exponent projection. [\[6\]](ltmctdimensionbase.md) A dimension over this set is built from its five exponents. [\[7\]](ltmctdimensionbase.md) Each of the five exponents of a product, a unit, an inverse, a quotient and a natural power follows from those of the factors. [\[8\]](ltmctdimensionbase.md) The generators L𝓭, T𝓭, M𝓭, C𝓭 and Θ𝓭 are the base vectors of the five base dimensions. [\[9\]](ltmctdimensionbase.md)
>
> The International System of Quantities has seven base quantities. [\[10\]](isqdimensionbase.md) In it electric charge is derived as current times time, with exponent one in current and in time and zero in mass. [\[11\]](isqdimensionbase.md) Amount of substance and luminous intensity are base dimensions of their own, distinct from the trivial dimension. [\[12\]](isqdimensionbase.md)
>
> A faithful embedding carries the LTMCT base dimensions into the ISQ set, sending the charge generator to the derived ISQ charge. [\[13\]](isqbridge.md) A reduction runs the other way, reading electric current as charge per time and forgetting amount of substance and luminous intensity. [\[14\]](isqbridge.md) The reduction is a retraction of the embedding, and the composite in the other order is not the identity. [\[15\]](isqbridge.md)
>
> ### Unit choices and the change of unit
>
> A unit choice fixes one unit for each of the five LTMCT base quantities, with the SI choice of metre, second, kilogram, coulomb and kelvin. [\[16\]](basic.md) … A second unit choice rescales each SI base unit by a distinct prime, which serves to refute dimensional correctness. [\[17\]](basic.md)
>
> The factor by which a quantity of a given dimension rescales under a change of unit choice is a monoid homomorphism from dimensions to the positive reals. [\[18\]](basic.md) It is one on the trivial dimension and on a unit system paired with itself. [\[19\]](basic.md) It is strictly positive and nonzero, composes along a chain of three unit choices, and inverts when the two choices are swapped. [\[20\]](basic.md) Scaling by it is injective. [\[21\]](basic.md) The factor is also available as a strictly positive real, that is as a unit of the non-negative reals, and it is by this that dimension-carrying quantities are scaled: no change of unit scales by zero, so the positive reals suffice, and taking them lets a type whose elements are strictly positive carry a dimension at all. [\[71\]](basic.md) This is the classical law for the change of a quantity under a change of unit \{4}.
>
> ### Unit systems over a general base set
>
> The change-of-unit law holds once for a general set of base dimensions and specialises to the LTMCT set and to the ISQ set without being restated. A magnitude layer assigns a positive real to each base dimension, with nonzero ratios. [\[26\]](parametricunits.md) On it the scaling homomorphism is the product over the base dimensions of the unit ratio raised to the corresponding exponent, and it is transitive. [\[27\]](parametricunits.md) A catalogue names a type of admissible units and a magnitude for each base dimension, and a unit system chooses exactly one unit per base dimension. [\[28\]](unitsystem.md) A unit system projects onto the magnitude layer. [\[29\]](unitsystem.md) The five-field LTMCT unit choice is equivalent to a unit system over the LTMCT base dimensions, and its scaling law is the generic product specialised to that set. [\[30\]](parametricunits.md)[\[31\]](unitsystem.md)
>
> Units of electric current, of amount of substance and of luminous intensity are each a positive magnitude, with a quotient by another unit of the same kind. [\[32\]](siunitchoices.md)[\[33\]](positiverealunit.md) The coherent SI units are the ampere, the mole and the candela. [\[34\]](siunitchoices.md) These unit types carry the same rescaling operation as the other five, so that a decimal multiple such as the milliampere exists. [\[37\]](siunitchoices.md)[\[38\]](positiverealunit.md) A unit choice over the seven ISQ base quantities fixes one unit for each, with the coherent SI choice of metre, kilogram, second, ampere, kelvin, mole and candela. [\[35\]](siunitchoices.md) Its scaling factor is the generic product over the ISQ base quantities. [\[36\]](siunitchoices.md) The SI base units are those of the SI Brochure \{5}.
>
> ### Dimension-carrying and unit-dependent types
>
> A type may carry a dimension, and the stronger notion is a type carrying a dimension on which the positive reals act. [\[22\]](basic.md) A function from unit choices to a dimension-carrying type has a dimension when it rescales by the factor of that dimension under every change of unit. [\[23\]](basic.md) The functions with this property form a subtype carrying a scalar action. [\[24\]](basic.md) For each fixed unit choice, a value of a dimension-carrying type is equivalent to a quantity given in every unit system, and reading that quantity back in the same unit choice returns the value. [\[25\]](basic.md)
>
> A unit-dependent type comes with a transformation of its elements under a change of unit, which composes along a chain of unit choices and is trivial on an unchanged choice. [\[39\]](unitdependent.md) Stronger versions require that transformation to commute with a scalar action, to be linear, or to be linear and continuous. [\[40\]](unitdependent.md) The transformation is then an equivalence, a linear map, a linear equivalence, a continuous linear map or a continuous linear equivalence. [\[41\]](unitdependent.md) The unit choices themselves and every dimension-carrying type are unit-dependent. [\[42\]](unitdependent.md) Carrying a dimension is enough for that on its own, whereas compatibility of the transformation with a non-negative scalar is meaningful only when such a scalar acts, and so is asked for separately. [\[72\]](unitdependent.md) Function types are unit-dependent, with the transformation acting on the argument, on the value, or on both. [\[43\]](unitdependent.md)
>
> A quantity or a statement is dimensionally correct when it is unchanged by a change of unit system; for functions this unfolds into conditions acting on the argument, on the value and on both. [\[44\]](unitdependent.md) The dimension-preserving product of two dimension-carrying types scales as the product of their dimensions. [\[45\]](unitdependent.md) The elements of a unit-dependent type that scale according to a prescribed dimension form a subset which itself carries that dimension. [\[46\]](unitdependent.md)
>
> ### Dimension-tagged values
>
> Values of an underlying type may be tagged with a dimension over any set of base dimensions. [\[47\]](withdim/basic.md) The tagged type inherits zero, addition, negation and subtraction, each computed on the underlying value. [\[48\]](withdim/basic.md) It inherits the order relations and the action of the positive reals. [\[49\]](withdim/basic.md) Multiplying or dividing real-valued tagged quantities multiplies or divides the underlying values and combines the dimensions in the same way. [\[50\]](withdim/basic.md) Over the LTMCT base dimensions a tagged type carries its dimension, and its transformation under a change of unit is scalar multiplication by the scaling factor. [\[51\]](withdim/basic.md) A tagged quantity of trivial dimension is unchanged by a change of unit. [\[52\]](withdim/basic.md) A cast moves a tagged quantity between two tags whose dimensions are equal, with the equality discharged automatically. [\[53\]](withdim/basic.md) A quantity whose elements are strictly positive is regarded as a dimension-tagged real by recording its magnitude, with the dimension read off its type so that the two cannot drift apart, and tagging it commutes both with a rescaling and with a change of unit. [\[73\]](withdim/basic.md)
>
> At a fixed numerical unit representation, tagged values form a real module without replacing the existing additive operations or the action of the nonnegative reals. [\[68\]](withdim/basic.md) They also form a normed space, and explicit coordinate equivalences transport functions and their Fréchet derivatives. [\[69\]](withdim/analysis.md) …
>
> ### Named quantities
>
> The base quantities themselves are the subject of the APIs for time \{6}, space \{7} and temperature \{8}, and of the mass and charge modules. Area has dimension length squared, with the square metre, square foot, square mile, are, hectare and acre, their values in SI units, and one acre equal to 43560 square feet. [\[54\]](withdim/area.md) Speed has dimension length over time, with the metre per second, mile per hour, kilometre per hour and knot, their values in SI units, and the conversions between them. [\[55\]](withdim/speed.md) Energy has dimension mass times length squared over time squared, with the joule, electronvolt, calorie and kilowatt hour. [\[56\]](withdim/energy.md) Pressure has dimension mass over length over time squared, with the pascal, millimetre of mercury, bar, standard atmosphere, torr and pound per square inch. [\[57\]](withdim/pressure.md) Momentum has dimension mass times length over time and takes values in d spatial components: it is the three-momentum rather than the four-momentum. [\[58\]](withdim/momentum.md) …
>
> ### Physical constants
>
> A physical constant is not a unit: it is a definite physical quantity, fixed once and for all, and the number recording it is determined by the unit system in which it is read. It is therefore recorded as a quantity given in every unit system rather than placed among the units of the quantity it measures. The speed of light is such a constant. Its type consists of strictly positive reals, which is why it needs the scaling by a strictly positive factor, and it carries the dimension of a length over a time; its value in our world is exactly 299792458 metres per second. [\[74\]](../relativity/speedoflight.md)[\[75\]](../relativity/speedoflight.md) The Boltzmann constant is recorded in the same way, with the dimension of an energy over a temperature and an exact value in our world. [\[77\]](../statisticalmechanics/boltzmannconstant.md) … There are units in which the speed of light and the Boltzmann constant are both one. [\[76\]](constants.md) …
>
> ### Calculus and dimensional correctness
>
> The derivative of a dimensionally correct differentiable function is dimensionally correct, and the derivative at a rescaled point is the explicitly rescaled derivative. [\[59\]](fderiv.md) The equation giving the derivative in a fixed direction as a quantity of the dimension of the target divided by the dimension of the source is dimensionally correct. [\[60\]](fderiv.md) A measure on a dimension-carrying type is unit-dependent, and the integral of a function whose dimension is that of its values divided by the dimension of the measure has the dimension of the values. [\[61\]](integral.md)
>
> ### Examples
>
> A length of 400 metres converts to miles. [\[62\]](examples.md) The relations E = m c^2 and F = m a, stated over dimension-tagged reals, are dimensionally correct. [\[63\]](examples.md) A speed as distance over time, an expression of mixed dimension in mass, temperature, current, length and time, and the cosine of an angular frequency times a time are each dimensionally correct. [\[64\]](examples.md) The relation E = m c is not dimensionally correct: a change of unit breaks it. [\[65\]](examples.md) The version of E = m c^2 written with the speed of light in an explicit unit system holds in SI units and, by transport, in every unit system. [\[66\]](examples.md)
>
> The equality of a length with a speed times a time holds propositionally rather than definitionally, so the two tagged types are bridged by a cast, and the same comparison works over a set of base dimensions with no physical unit system, namely bits and symbols. [\[67\]](parametricdimensionexamples.md)
>
> The harmonic oscillator carries its mass and spring constant with their physical dimensions. Its potential energy is assembled from dimension-tagged quantities, agrees in coordinates with the numerical oscillator, and has its derivative from the generic transport of derivatives. [\[70\]](../classicalmechanics/harmonicoscillator/withdim.md)

Its references:

> - \{1\} ISO/IEC 80000-1:2009, *Quantities and units, Part 1: General*, Clauses 3 to 6 (quantities, systems of quantities, dimensions, and systems of units).
> - \{2\} JCGM 200:2012, *International vocabulary of metrology* (VIM, 3rd edition), Clause 1 (base quantity, derived quantity, quantity dimension, base unit, coherent system of units).
> - \{3\} Lean Zulip, #Physlib > physical units, https://leanprover.zulipchat.com/#narrow/channel/479953-Physlib/topic/physical.20units
> - \{4\} G. I. Barenblatt, *Scaling, Self-similarity, and Intermediate Asymptotics*, Cambridge University Press (1996), Chapter 1, Sections 1.1 and 1.2 (dimensions, systems of units, and the change of a quantity under a change of unit).
> - \{5\} International Bureau of Weights and Measures (BIPM), *The International System of Units (SI Brochure)*, 9th edition (2019), Chapter 1 (quantities and units) and Chapter 2 (the defining constants and the seven base units).
> - \{6\} Time API map — [Physlib/SpaceAndTime/Time/API-map.md](../spaceandtime/time/README.md)
> - \{7\} Space API map — [Physlib/SpaceAndTime/Space/API-map.md](../spaceandtime/space/README.md)
> - \{8\} Temperature API map — [Physlib/Thermodynamics/Temperature/API-map.md](../thermodynamics/temperature/README.md)

- [Dimensions and unit](basic.md)
- [Physical constants](constants.md)
- [Dimension](dimension.md)
- [Examples of units in Physlib](examples.md)
- [Reducible rational arithmetic for dimension exponents](exponent.md)
- [Dimensional invariance of fderiv](fderiv.md)
- [Dimensional invariance of the integral](integral.md)
- [Bridging PhysLib's default basis and the ISQ basis](isqbridge.md)
- [The ISQ base quantities](isqdimensionbase.md)
- [PhysLib's default dimension basis](ltmctdimensionbase.md)
- [Examples: parametric dimensions and comparing dimensioned quantities](parametricdimensionexamples.md)
- [The unit side, parametrised in the same basis](parametricunits.md)
- [A. Shared arithmetic for positive-real unit types](positiverealunit.md)
- [A typed unit choice over the ISQ base quantities (the SI units)](siunitchoices.md)
- [Physlib.Units.UnitDependent](unitdependent.md)
- [Unit systems, parametrised in a dimension basis](unitsystem.md)
- [WithDim](withdim/README.md)
