# Blackbody

The folder [Physlib/QuantumMechanics/Blackbody/](https://github.com/leanprover-community/physlib/tree/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/QuantumMechanics/Blackbody): 1 module, with an article.

The repository's API map for this folder, *Blackbody radiation* ([Physlib/QuantumMechanics/Blackbody/API-map.md](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/QuantumMechanics/Blackbody/API-map.md)): its Content section, with the sentences it marks as not yet formalized left out (…). A citation \[n\] links the module its n-th Lean reference names.

*Content (Alpha)*

> ### Frequency and wavelength spectra
>
> A black body is specified by its temperature. For positive frequency $\nu$ and temperature $T$, its spectral radiance per unit frequency is given by Planck's law, $B_\nu(T)=2h\nu^3/[c^2(\exp(h\nu/(k_B T))-1)]$. This radiance is positive in that domain and vanishes at zero frequency and at absolute zero. [\[1\]](planckslaw.md)
>
> The wavelength density at $\lambda>0$ measures radiance over an interval in wavelength. At positive temperature, the change of variable $\nu=c/\lambda$ gives $B_\lambda(T)=(c/\lambda^2) B_\nu(T)|_{\nu=c/\lambda}$, where $c/\lambda^2$ is the magnitude of the Jacobian. [\[2\]](planckslaw.md)
>
> ### Energy per mode and the classical comparison
>
> A mode of frequency $\nu>0$ is modeled by an oscillator with level spacing $\varepsilon=h\nu$. In the canonical ensemble \{1}, its levels have energies $n\varepsilon$ for nonnegative integers $n$. At positive temperature, the mean energy is $\varepsilon/(\exp(\beta\varepsilon)-1)$, with $\beta=1/(k_B T)$. The corresponding classical model integrates over positive energies with Lebesgue measure and has mean energy $k_B T$. [\[3\]](../../../physlibalpha/quantummechanics/blackbody/rayleighjeans.md)
>
> Multiplying each mean energy by the same factor $2\nu^2/c^2$ gives Planck's spectral radiance and the Rayleigh–Jeans spectral radiance, respectively. The quantized mean energy is strictly below the classical one, so Planck's radiance is strictly below Rayleigh–Jeans at every positive frequency and positive temperature. [\[4\]](../../../physlibalpha/quantummechanics/blackbody/rayleighjeans.md)\[5\]

Its references:

> - \{1\} Canonical ensemble API map — [Physlib/StatisticalMechanics/CanonicalEnsemble/API-map.md](../../statisticalmechanics/canonicalensemble/README.md)

- [Planck's Law](planckslaw.md)
