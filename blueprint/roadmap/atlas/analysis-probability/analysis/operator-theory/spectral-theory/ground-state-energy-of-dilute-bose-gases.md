---
declaration: section
origin: cited
lean: MathlibExt.Geometry.BoseGasesWanted.BoseGases.box, MathlibExt.Geometry.BoseGasesWanted.BoseGases.CInfty0Box, MathlibExt.Geometry.BoseGasesWanted.BoseGases.IsRadial, MathlibExt.Geometry.BoseGasesWanted.BoseGases.IsScatteringSolution, MathlibExt.Geometry.BoseGasesWanted.BoseGases.a, MathlibExt.Geometry.BoseGasesWanted.BoseGases.𝓡, MathlibExt.Geometry.BoseGasesWanted.BoseGases.η, MathlibExt.Geometry.BoseGasesWanted.BoseGases.𝓒
statement: formalized
---

# Ground-state energy of dilute Bose gases

9 results, 6 proved and 3 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/ground-state-energy-of-dilute-bose-gases/index.html).

## The box $((0,L)^3)^N$

For a natural number $N$ and a real number $L$, the box
$([0,L]^3)^N$ is the set of configurations $(x_1, \dots, x_N)$ of $N$ points of $\mathbb{R}^3$
such that every coordinate of every point $x_i$ lies in the closed interval $[0, L]$.

Formalized by `MathlibExt.Geometry.BoseGasesWanted.BoseGases.box`, a definition declared in [WantedExt/Geometry/BoseGasesWanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/BoseGasesWanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/ground-state-energy-of-dilute-bose-gases/index.html#box).

## Smooth functions supported inside the box

For a natural number $N$ and a real number
$L$, $C_0^\infty(([0,L]^3)^N) \setminus \{0\}$ consists of the functions
$\Psi : (\mathbb{R}^3)^N \to \mathbb{R}$ that are smooth on the box $([0,L]^3)^N$, whose closed
support is contained in the interior of the box, and that are not identically zero.

The functions are defined on all of $(\mathbb{R}^3)^N$ rather than on the box only.

Formalized by `MathlibExt.Geometry.BoseGasesWanted.BoseGases.CInfty0Box`, a structure declared in [WantedExt/Geometry/BoseGasesWanted.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/BoseGasesWanted.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/ground-state-energy-of-dilute-bose-gases/index.html#cinfty0-box).

## Radial functions

A function $v : \mathbb{R}^3 \to \mathbb{R}$ is radial if
$v(x) = v(y)$ for all $x, y \in \mathbb{R}^3$ with $\|x\| = \|y\|$.

Formalized by `MathlibExt.Geometry.BoseGasesWanted.BoseGases.IsRadial`, a definition declared in [WantedExt/Geometry/BoseGasesWanted.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/BoseGasesWanted.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/ground-state-energy-of-dilute-bose-gases/index.html#is-radial).

## Scattering solutions

Let $v, w : \mathbb{R}^3 \to \mathbb{R}$. The function $w$ is a
scattering solution for the potential $v$ if $w$ and $v\,(1 - w)$ are locally integrable,
$w(x) \to 0$ as $\|x\| \to \infty$, and $w$ solves the scattering equation
$-\Delta w = \frac{1}{2} v\,(1 - w)$ (Equation (3.4) of Fournais–Solovej) in the weak sense:
for every smooth, compactly supported $\varphi : \mathbb{R}^3 \to \mathbb{R}$,

$$-\int_{\mathbb{R}^3} w\,\Delta\varphi = \frac{1}{2} \int_{\mathbb{R}^3} v\,(1 - w)\,\varphi.$$

Formalized by `MathlibExt.Geometry.BoseGasesWanted.BoseGases.IsScatteringSolution`, a structure declared in [WantedExt/Geometry/BoseGasesWanted.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/BoseGasesWanted.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/ground-state-energy-of-dilute-bose-gases/index.html#is-scattering-solution).

## Scattering length

Let $v : \mathbb{R}^3 \to \mathbb{R}$ be a potential. If there is a
radial scattering solution $w$ to the scattering equation with potential $v$, the scattering
length of $v$ is $a(v) = (8\pi)^{-1} \int_{\mathbb{R}^3} v(x)\,(1 - w(x))\,dx$, where $w$ is
one such solution, chosen arbitrarily; if there is no radial scattering solution, $a(v) = 0$.

This is Equation (3.5) of Fournais–Solovej. Under the assumptions of Theorem 1.2 the radial
scattering solution exists and is unique, so the choice does not matter there.

Formalized by `MathlibExt.Geometry.BoseGasesWanted.BoseGases.a`, a definition declared in [WantedExt/Geometry/BoseGasesWanted.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/BoseGasesWanted.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/ground-state-energy-of-dilute-bose-gases/index.html#a).

## The ratio $\mathcal{R}(v)$

For a potential $v : \mathbb{R}^3 \to \mathbb{R}$ with
scattering length $a(v)$, let $\mathcal{R}(v) = \int_{\mathbb{R}^3} v(x)/(8\pi a(v))\,dx$. When
$a(v) \neq 0$ this is the ratio of $(8\pi)^{-1} \int v$ to $a(v)$.

Formalized by `MathlibExt.Geometry.BoseGasesWanted.BoseGases.𝓡`, a definition declared in [WantedExt/Geometry/BoseGasesWanted.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/BoseGasesWanted.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/ground-state-energy-of-dilute-bose-gases/index.html#untitled).

## Lee–Huang–Yang error exponent

$\eta$ is a real constant, not given explicitly, that
serves as the exponent in the error term $(\rho a^3)^{1/2 + \eta}$ of the Lee–Huang–Yang lower
bound (Theorem 1.2), where $\rho$ is the density and $a$ the scattering length of the
potential; that theorem asserts $\eta > 0$.

## Sources

- S. Fournais and J. P. Solovej, `The energy of dilute Bose gases`, Annals of Math, 192 (3) 2020. Statement taken from https://github.com/ImperialCollegeLondon/AnnalsChallenge. Problem `annals_bose_gases` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Geometry.BoseGasesWanted.BoseGases.η` is written with `def_wanted` in [WantedExt/Geometry/BoseGasesWanted.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/BoseGasesWanted.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/ground-state-energy-of-dilute-bose-gases/index.html#untitled-2).

## Lee–Huang–Yang error constant

$\mathcal{C}$ is a real-valued function of two real
variables, not given explicitly. Let $v$ be a potential with scattering length $a$ whose closed
support lies in the open ball $B(0, R)$, and let $\mathcal{R}(v) = \int v/(8\pi a)$. In the
Lee–Huang–Yang lower bound (Theorem 1.2) for $v$ at density $\rho$, the error term is
$\mathcal{C}(\mathcal{R}(v), R/a)\,(\rho a^3)^{1/2 + \eta}$, where $\eta$ is the Lee–Huang–Yang
error exponent, so its constant depends only on $\mathcal{R}(v)$ and $R/a$.

## Sources

- S. Fournais and J. P. Solovej, `The energy of dilute Bose gases`, Annals of Math, 192 (3) 2020. Statement taken from https://github.com/ImperialCollegeLondon/AnnalsChallenge. Problem `annals_bose_gases` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Geometry.BoseGasesWanted.BoseGases.𝓒` is written with `def_wanted` in [WantedExt/Geometry/BoseGasesWanted.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/BoseGasesWanted.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/ground-state-energy-of-dilute-bose-gases/index.html#untitled-3).

## Lee–Huang–Yang lower bound for dilute Bose gases

There are a real number $\eta$ and a
function $\mathcal{C}$ of two real variables such that the following holds. Let
$v : \mathbb{R}^3 \to \mathbb{R}$ be a non-negative, radial, integrable potential that is not
almost everywhere zero, and let $R > 0$ be such that the closed support of $v$ lies in the open
ball $B(0, R)$. Let $a$ be the scattering length of $v$, let $\mathcal{R}(v) = \int v/(8\pi a)$,
and let $e(\rho, v)$ be the ground state energy density at density $\rho$: the limit, as
$L \to \infty$ and $N/L^3 \to \rho$, of $L^{-3}$ times the infimum, over
$\Psi \in C_0^\infty(([0,L]^3)^N) \setminus \{0\}$, of
$\langle \Psi, H_N \Psi \rangle / \|\Psi\|^2$, where the inner product and norm are those of
$L^2(([0,L]^3)^N)$ and, writing points of $(\mathbb{R}^3)^N$ as $(x_1, \dots, x_N)$ and
$\Delta_{x_i}$ for the Laplacian in the variable $x_i$,
$H_N = \sum_{i=1}^{N} -\Delta_{x_i} + \sum_{1 \le i < j \le N} v(x_i - x_j)$. Then
$\eta > 0$, and for all sufficiently small $\rho > 0$,

$$
e(\rho, v) \ge 4\pi\rho^2 a \left(1 + \frac{128}{15\sqrt{\pi}}\sqrt{\rho a^3} -
\mathcal{C}(\mathcal{R}(v), R/a)\,(\rho a^3)^{1/2 + \eta}\right).
$$

The source takes the limit $\rho a^3 \to 0^+$; for fixed $v$ this is the same as $\rho \to 0^+$.
Although the wording of Theorem 1.2 in the source suggests that $\eta$ may depend on
$\mathcal{R}(v)$ and $R/a$, Theorem 6.8 there shows that $\eta$ is a universal constant.

## Sources

- S. Fournais and J. P. Solovej, `The energy of dilute Bose gases`, Annals of Math, 192 (3) 2020. Statement taken from https://github.com/ImperialCollegeLondon/AnnalsChallenge. Problem `annals_bose_gases` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Geometry.BoseGasesWanted.BoseGases.theorem_1_2` is written with `theorem_wanted` in [WantedExt/Geometry/BoseGasesWanted.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/BoseGasesWanted.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/ground-state-energy-of-dilute-bose-gases/index.html#theorem-1-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Ground-state energy of dilute Bose gases](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/ground-state-energy-of-dilute-bose-gases/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/operator-theory/spectral-theory/ground-state-energy-of-dilute-bose-gases)
