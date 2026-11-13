---
declaration: section
origin: cited
lean: MetaMathlibExt.haymanAuxiliaryA, MetaMathlibExt.haymanAuxiliaryB, MetaMathlibExt.IsHaymanAdmissible, MetaMathlibExt.hayman_coefficient_asymptotic
statement: formalized
proof: formalized
---

# Hayman admissibility

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/hayman-admissibility/index.html).

## Hayman auxiliary function $A$

For a function $G : \mathbb{C} \to \mathbb{C}$ and a real
number $r$, $A(r)$ is the real part of $r\,G'(r)/G(r)$, where $G'$ is the complex derivative of
$G$.

Formalized by `MetaMathlibExt.haymanAuxiliaryA`, a definition declared in [MathlibExt/Analysis/Complex/HaymanAdmissibility.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/HaymanAdmissibility.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/hayman-admissibility/index.html#hayman-auxiliary-a).

## Hayman auxiliary function $B$

For a function $G : \mathbb{C} \to \mathbb{C}$ and a real
number $r$, $B(r) = r\,A'(r)$, where $A$ is the Hayman auxiliary function of $G$, viewed as a
real function of $r$, and $A'$ is its derivative.

Formalized by `MetaMathlibExt.haymanAuxiliaryB`, a definition declared in [MathlibExt/Analysis/Complex/HaymanAdmissibility.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/HaymanAdmissibility.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/hayman-admissibility/index.html#hayman-auxiliary-b).

## Hayman-admissible function (finite radius)

Let $G : \mathbb{C} \to \mathbb{C}$, let
$R_0$ and $\rho$ be real numbers, write $G'$ for the complex derivative of $G$ and $A$, $B$ for
the Hayman auxiliary functions of $G$, and say that a property holds for $r$ near $\rho$ if there
is $\eta > 0$ such that it holds for every $r \in (R_0, \rho)$ with $r > \rho - \eta$. Then $G$ is
Hayman admissible on $(R_0, \rho)$ when $0 < R_0 < \rho$; $G$ is analytic on the open disk
$|z| < \rho$; for every $r \in (R_0, \rho)$, $G(r)$ is a positive real number and
$r\,G'(r)/G(r)$ is real; $A(r) \to \infty$ and $B(r) \to \infty$ as $r$ tends to $\rho$ within
$(R_0, \rho)$; and there is a function $\delta : \mathbb{R} \to \mathbb{R}$ with
$0 < \delta(r) < \pi$ for $r$ near $\rho$ such that for every $\varepsilon > 0$ and all $r$ near
$\rho$, every real $\theta$ with $|\theta| \le \delta(r)$ satisfies the locality estimate

$$\left|G(re^{i\theta}) - G(r)\,e^{i\theta A(r) - \theta^2 B(r)/2}\right|
\le \varepsilon \left|G(r)\,e^{i\theta A(r) - \theta^2 B(r)/2}\right|,$$

and every real $\theta$ with $\delta(r) \le |\theta| < \pi$ satisfies the decay estimate
$|G(re^{i\theta})| \le \varepsilon\,|G(r)|/\sqrt{B(r)}$.

The capture, locality and decay conditions follow the Flajolet-Sedgewick formulation rather than
the abbreviated maximum-modulus restatement (Jiyou Li, "Asymptotic Estimate for the Multinomial
Coefficients", Journal of Integer Sequences 23 (2020), Article 20.1.3, Lemma [Hayman] `lem2`),
whose maximum-modulus condition is insufficient as stated and is not used.

Formalized by `MetaMathlibExt.IsHaymanAdmissible`, a definition declared in [MathlibExt/Analysis/Complex/HaymanAdmissibility.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/HaymanAdmissibility.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/hayman-admissibility/index.html#is-hayman-admissible).

## Hayman's coefficient asymptotic (finite radius)

Let $G : \mathbb{C} \to \mathbb{C}$ be
Hayman admissible on $(R_0, \rho)$, with Hayman auxiliary functions $A$ and $B$. Let
$(c_n)_{n \ge 0}$ be complex numbers such that $\sum_{n \ge 0} c_n z^n$ converges absolutely to
$G(z)$ for every complex $z$ with $|z| < \rho$, and let $(r_n)_{n \ge 0}$ be real numbers such
that for all sufficiently large $n$, $r_n \in (R_0, \rho)$, $A(r_n) = n$, and $r_n$ is the only
$r \in (R_0, \rho)$ with $A(r) = n$. Then, as $n \to \infty$,

$$c_n \sim \frac{G(r_n)}{r_n^n \sqrt{2\pi B(r_n)}}.$$

Proof: The saddle converges to the finite radius, Cauchy's coefficient integral is split at the
admissibility cutoff, and the central Gaussian term and decaying tails are normalized separately.

## Sources

- arXiv:1906.07169v2, tex lines 495-506.

Formalized by `MetaMathlibExt.hayman_coefficient_asymptotic`, a theorem declared in [MathlibExt/Analysis/Complex/HaymanAdmissibility.lean, line 877](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/HaymanAdmissibility.lean#L877). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/hayman-admissibility/index.html#hayman-coefficient-asymptotic).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hayman admissibility](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/hayman-admissibility/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/complex-analysis/entire-functions/hayman-admissibility)
