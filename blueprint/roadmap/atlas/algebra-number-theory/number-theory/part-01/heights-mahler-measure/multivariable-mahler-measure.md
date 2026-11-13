---
declaration: section
origin: cited
lean: LogarithmicMahlerMeasure.realSum, LogarithmicMahlerMeasure.torusCharacter, LogarithmicMahlerMeasure.torusCharacterHom, LogarithmicMahlerMeasure.torusEval, LogarithmicMahlerMeasure.normalizedBoxIntegral, LogarithmicMahlerMeasure.logarithmicMahlerMeasure, LogarithmicMahlerMeasure.finOneAddEquiv, LogarithmicMahlerMeasure.bridgeLaurent
statement: formalized
proof: formalized
---

# Multivariable Mahler measure

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/multivariable-mahler-measure/index.html).

## Phase of an exponent vector

For an angle vector $\theta \in \mathbb{R}^n$ and an exponent
vector $e \in \mathbb{Z}^n$, the real phase of $e$ at $\theta$ is $\sum_{j} e_j \theta_j$.

Formalized by `LogarithmicMahlerMeasure.realSum`, a definition declared in [MathlibExt/Analysis/Polynomial/MultivariableMahlerMeasure.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Polynomial/MultivariableMahlerMeasure.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/multivariable-mahler-measure/index.html#real-sum).

## Torus character

For an angle vector $\theta \in \mathbb{R}^n$, the torus character at
$\theta$ sends an exponent vector $e \in \mathbb{Z}^n$ to
$\exp\bigl(i \sum_{j} e_j \theta_j\bigr) \in \mathbb{C}$.

Formalized by `LogarithmicMahlerMeasure.torusCharacter`, a definition declared in [MathlibExt/Analysis/Polynomial/MultivariableMahlerMeasure.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Polynomial/MultivariableMahlerMeasure.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/multivariable-mahler-measure/index.html#torus-character).

## Torus character as a monoid homomorphism

For an angle vector $\theta \in \mathbb{R}^n$,
the torus character $e \mapsto \exp\bigl(i \sum_{j} e_j \theta_j\bigr)$, viewed as a map from the
additive group $\mathbb{Z}^n$ written multiplicatively to the multiplicative monoid of
$\mathbb{C}$, is a monoid homomorphism: it sends $0$ to $1$ and sums to products.

Formalized by `LogarithmicMahlerMeasure.torusCharacterHom`, a definition declared in [MathlibExt/Analysis/Polynomial/MultivariableMahlerMeasure.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Polynomial/MultivariableMahlerMeasure.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/multivariable-mahler-measure/index.html#torus-character-hom).

## Evaluation on the unit torus

For an angle vector $\theta \in \mathbb{R}^n$, evaluation at
the point $(\exp(i\theta_1), \dots, \exp(i\theta_n))$ of the unit torus is the
$\mathbb{C}$-algebra homomorphism from complex Laurent polynomials in $n$ variables to
$\mathbb{C}$ that, writing $X^e$ for the monomial with exponent vector $e \in \mathbb{Z}^n$,
sends $\sum_e c_e X^e$ to $\sum_e c_e \exp\bigl(i \sum_{j} e_j \theta_j\bigr)$.

Formalized by `LogarithmicMahlerMeasure.torusEval`, a definition declared in [MathlibExt/Analysis/Polynomial/MultivariableMahlerMeasure.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Polynomial/MultivariableMahlerMeasure.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/multivariable-mahler-measure/index.html#torus-eval).

## Normalized box integral

For a function $f \colon \mathbb{R}^m \to \mathbb{R}$, the
normalized box integral of $f$ is $(2\pi)^{-m} \int_{[0, 2\pi]^m} f(x) \, dx$, the integral taken
with respect to Lebesgue measure (and equal to $0$ when $f$ is not integrable on the box).

Formalized by `LogarithmicMahlerMeasure.normalizedBoxIntegral`, a definition declared in [MathlibExt/Analysis/Polynomial/MultivariableMahlerMeasure.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Polynomial/MultivariableMahlerMeasure.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/multivariable-mahler-measure/index.html#normalized-box-integral).

## Logarithmic Mahler measure

For a complex Laurent polynomial $F$ in $m$ variables, the
logarithmic Mahler measure of $F$ is the real number
$(2\pi)^{-m} \int_{[0, 2\pi]^m} \log |F(e^{i\theta_1}, \dots, e^{i\theta_m})| \, d\theta$,
the integral taken with respect to Lebesgue measure.

The cited source applies this formula to nonzero polynomials. As with Mathlib's logarithmic
Mahler measure of one-variable polynomials, the definition here is total: $\log 0 = 0$ and a
non-integrable function has integral $0$, so in particular the value at $F = 0$ is $0$.

Formalized by `LogarithmicMahlerMeasure.logarithmicMahlerMeasure`, a definition declared in [MathlibExt/Analysis/Polynomial/MultivariableMahlerMeasure.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Polynomial/MultivariableMahlerMeasure.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/multivariable-mahler-measure/index.html#logarithmic-mahler-measure).

## Integer vectors of length one

The additive isomorphism from $\mathbb{Z}^1$, the group of
functions $\{0\} \to \mathbb{Z}$ under pointwise addition, to $\mathbb{Z}$ that sends a function
$e$ to its value $e(0)$.

Formalized by `LogarithmicMahlerMeasure.finOneAddEquiv`, a definition declared in [MathlibExt/Analysis/Polynomial/MultivariableMahlerMeasure.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Polynomial/MultivariableMahlerMeasure.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/multivariable-mahler-measure/index.html#fin-one-add-equiv).

## Identification of one-variable Laurent polynomials

The $\mathbb{C}$-algebra isomorphism
from complex Laurent polynomials whose exponents are vectors $e \in \mathbb{Z}^1$ (functions
$\{0\} \to \mathbb{Z}$) to complex Laurent polynomials $\mathbb{C}[T, T^{-1}]$ in one variable,
induced by the additive isomorphism $\mathbb{Z}^1 \cong \mathbb{Z}$, $e \mapsto e(0)$. Writing
$X^{e}$ for the monomial with exponent vector $e$, it sends $c\,X^{e}$ to $c\,T^{e(0)}$.

Formalized by `LogarithmicMahlerMeasure.bridgeLaurent`, a definition declared in [MathlibExt/Analysis/Polynomial/MultivariableMahlerMeasure.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Polynomial/MultivariableMahlerMeasure.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/multivariable-mahler-measure/index.html#bridge-laurent).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Multivariable Mahler measure](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/multivariable-mahler-measure/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/heights-mahler-measure/multivariable-mahler-measure)
