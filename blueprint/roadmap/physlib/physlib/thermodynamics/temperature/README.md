# Temperature

The folder [Physlib/Thermodynamics/Temperature/](https://github.com/leanprover-community/physlib/tree/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Thermodynamics/Temperature): 2 modules, an article each, in path order with Basic.lean first in its folder.

The repository's API map for this folder, *Temperature* ([Physlib/Thermodynamics/Temperature/API-map.md](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Thermodynamics/Temperature/API-map.md)), with the sentences it marks as not yet formalized left out (…). A citation \[n\] links the module its n-th Lean reference names.

*Content (Alpha)*

> ### Absolute temperature and inverse temperature
>
> An absolute temperature is a nonnegative real in an arbitrary scale that puts absolute zero at zero; it coerces to the nonnegative reals and to the reals, carries a topology and a zero, and is determined by its value. [\[1\]](basic.md) This excludes the negative absolute temperatures that a system with a bounded energy spectrum can carry \{1}. A temperature is built from a nonnegative real, or from a real together with a proof that it is nonnegative. [\[7\]](basic.md) The temperature enters the Gibbs distribution through its inverse \{2}. A temperature has an inverse temperature, formed with the Boltzmann constant [\[14\]](../../statisticalmechanics/boltzmannconstant.md) , and a temperature is recovered from an inverse temperature. [\[2\]](basic.md) Passing to the inverse temperature and back is the identity, in both directions. [\[3\]](basic.md) A strictly positive temperature has a strictly positive inverse temperature. [\[4\]](basic.md) The boundary value zero is paired with itself, which is a convention of the underlying nonnegative reals rather than a physical statement.
>
> The temperature is a continuous function of the inverse temperature at positive inverse temperature, and its real coordinate is differentiable on the positive reals. [\[5\]](basic.md) In the limit of large inverse temperature the temperature is eventually positive and converges to absolute zero from above, the regime in which a system settles into its lowest energy states. [\[6\]](basic.md) At positive temperature the inverse temperature has a derivative with respect to the temperature, and the chain rule converts a derivative in one variable into a derivative in the other. [\[8\]](basic.md)
>
> ### Temperature scales
>
> A temperature unit is a choice of scale, carrying a positive scale factor. [\[9\]](temperatureunits.md)[\[10\]](../../units/positiverealunit.md) Two temperature units have a ratio, a nonnegative real, which is positive and behaves reflexively, symmetrically and multiplicatively along a chain of units. [\[11\]](../../units/positiverealunit.md) A temperature unit rescales by a positive real, with the ratios this induces and its composition law. [\[12\]](../../units/positiverealunit.md) Kelvin is the reference temperature unit, and the other units, among them the nanokelvin, microkelvin, millikelvin and the absolute Fahrenheit-sized degree, are obtained from it by rescaling. [\[13\]](temperatureunits.md)

Its references:

> - \{1\} N. F. Ramsey, Thermodynamics and statistical mechanics at negative absolute temperatures, *Physical Review* 103 (1956), 20-28.
> - \{2\} L. D. Landau and E. M. Lifshitz, *Statistical Physics, Part 1*, §9 (temperature) and §31 (the Gibbs distribution).

- [Temperature](basic.md)
- [Units on Temperature](temperatureunits.md)
