---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.DeBruijnNewman.phiTerm, MathlibExt.NumberTheory.DeBruijnNewman.phi, MathlibExt.NumberTheory.DeBruijnNewman.H, MathlibExt.NumberTheory.DeBruijnNewman.ZerosAllReal, MathlibExt.NumberTheory.DeBruijnNewman.deBruijnNewmanConstant, MathlibExt.NumberTheory.DeBruijnNewmanWanted.rodgersTaoNegativeTime_wanted, MathlibExt.NumberTheory.DeBruijnNewmanWanted.plattTrudgianUpperBound_wanted
statement: formalized
---

# De Bruijn–Newman constant

7 results, 5 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/de-bruijn-newman-constant/index.html).

## Summands of Newman's kernel

For real $u$ and a natural number $n$, the $n$-th summand
of Newman's kernel, counted from $n = 0$, is

$$\left(2\pi^2 (n+1)^4 e^{9u} - 3\pi (n+1)^2 e^{5u}\right) e^{-\pi (n+1)^2 e^{4u}}.$$

Formalized by `MathlibExt.NumberTheory.DeBruijnNewman.phiTerm`, a definition declared in [MathlibExt/NumberTheory/DeBruijnNewman.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/DeBruijnNewman.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/de-bruijn-newman-constant/index.html#phi-term).

## Newman's kernel

For real $u$, Newman's kernel is the sum of the series

$$\Phi(u) = \sum_{n=1}^{\infty} (2\pi^2 n^4 e^{9u} - 3\pi n^2 e^{5u}) e^{-\pi n^2 e^{4u}},$$

which converges absolutely for every real $u$.

Formalized by `MathlibExt.NumberTheory.DeBruijnNewman.phi`, a definition declared in [MathlibExt/NumberTheory/DeBruijnNewman.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/DeBruijnNewman.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/de-bruijn-newman-constant/index.html#phi).

## The de Bruijn–Newman deformation

For real $\lambda$ and complex $z$,

$$H_\lambda(z) = \int_0^\infty e^{\lambda u^2}\, \Phi(u) \cos(zu)\, du,$$

where $\Phi$ is Newman's kernel and the integral runs over $u > 0$.

The integral is a Lebesgue integral, taken to be $0$ when the integrand is not integrable.

Formalized by `MathlibExt.NumberTheory.DeBruijnNewman.H`, a definition declared in [MathlibExt/NumberTheory/DeBruijnNewman.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/DeBruijnNewman.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/de-bruijn-newman-constant/index.html#h).

## Real-rootedness of the de Bruijn–Newman deformation

For real $\lambda$, this is the
statement that every zero of the de Bruijn–Newman deformation $H_\lambda$ is real: every complex
$z$ with $H_\lambda(z) = 0$ has imaginary part $0$.

Formalized by `MathlibExt.NumberTheory.DeBruijnNewman.ZerosAllReal`, a definition declared in [MathlibExt/NumberTheory/DeBruijnNewman.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/DeBruijnNewman.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/de-bruijn-newman-constant/index.html#zeros-all-real).

## The de Bruijn–Newman constant

The de Bruijn–Newman constant $\Lambda$ is the infimum of
the set of real numbers $\lambda$ such that every zero of the de Bruijn–Newman deformation
$H_\lambda$ is real. The infimum is taken in $\mathbb{R}$, with the convention that it is $0$
when this set is empty or not bounded below.

Newman's theorem, that every zero of $H_\lambda$ is real exactly when $\lambda \ge \Lambda$, is
not part of this definition.

Formalized by `MathlibExt.NumberTheory.DeBruijnNewman.deBruijnNewmanConstant`, a definition declared in [MathlibExt/NumberTheory/DeBruijnNewman.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/DeBruijnNewman.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/de-bruijn-newman-constant/index.html#de-bruijn-newman-constant).

## Nonreal zeros of the de Bruijn–Newman deformation at negative times

For every real
$\lambda < 0$, not every zero of the de Bruijn–Newman deformation $H_\lambda$ is real: there is
a complex $z$ with $H_\lambda(z) = 0$ and nonzero imaginary part.

## Sources

- Rodgers and Tao, *The de Bruijn--Newman constant is non-negative*, Forum Math. Pi 8 (2020): at every negative deformation time, `H` has a nonreal zero.

Stated but not proved: `MathlibExt.NumberTheory.DeBruijnNewmanWanted.rodgersTaoNegativeTime_wanted` is written with `theorem_wanted` in [WantedExt/NumberTheory/DeBruijnNewmanWanted.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DeBruijnNewmanWanted.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/de-bruijn-newman-constant/index.html#rodgers-tao-negative-time-wanted).

## All zeros of the de Bruijn–Newman deformation are real at time 1/5

Every zero of the
de Bruijn–Newman deformation $H_{1/5}$ is real: every complex $z$ with $H_{1/5}(z) = 0$ has
imaginary part $0$.

## Sources

- Platt and Trudgian, *The Riemann hypothesis is true up to 3·10¹²*, Bull. Lond. Math. Soc. 53 (2021), via the Polymath15 criterion: at time `1 / 5` all zeros of `H` are real (catalogue upper bound `0.2`).

Stated but not proved: `MathlibExt.NumberTheory.DeBruijnNewmanWanted.plattTrudgianUpperBound_wanted` is written with `theorem_wanted` in [WantedExt/NumberTheory/DeBruijnNewmanWanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DeBruijnNewmanWanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/de-bruijn-newman-constant/index.html#platt-trudgian-upper-bound-wanted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: De Bruijn–Newman constant](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/de-bruijn-newman-constant/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/de-bruijn-newman-constant)
