---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.CalegariDimitrovTangLinearIndependentWanted.NumberTheory.CalegariDimitrovTangLinearIndependent.cdt_linearIndependent, MathlibExt.NumberTheory.LindemannWanted.hermite_lindemann
statement: formalized
---

# Transcendence and irrationality: its own results

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/transcendence-irrationality/index.html).

Hermite–Lindemann, Lindemann–Weierstrass, Gelfond–Schneider, Mahler functions, irrationality and linear independence of constants.

## Calegari–Dimitrov–Tang linear independence theorems

Let
$\chi : \mathbb{Z}/3\mathbb{Z} \to \mathbb{C}$ be given by $\chi(0) = 0$, $\chi(1) = 1$ and
$\chi(2) = -1$ (the nontrivial Dirichlet character modulo $3$), let $\zeta$ be the Riemann zeta
function and let $L(s, \chi)$ be the Dirichlet $L$-function of $\chi$. Then the complex numbers
$1$, $\zeta(2)$ and $L(2, \chi)$ are linearly independent over $\mathbb{Q}$. Moreover, let $m$
and $n$ be integers, neither of them equal to $-1$ or $0$, with $10^6 |m - n| < |n|$, and put
$\ell_m = \log(1 + 1/m)$ and $\ell_n = \log(1 + 1/n)$. Then $\ell_m \ell_n$ is irrational, and if
$m \ne n$, the real numbers $1$, $\ell_m$, $\ell_n$ and $\ell_m \ell_n$ are linearly independent
over $\mathbb{Q}$.

## Sources

- https://arxiv.org/abs/2408.15403. Problem `cdt_linearIndependent` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.NumberTheory.CalegariDimitrovTangLinearIndependentWanted.NumberTheory.CalegariDimitrovTangLinearIndependent.cdt_linearIndependent` is written with `theorem_wanted` in [WantedExt/NumberTheory/CalegariDimitrovTangLinearIndependentWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CalegariDimitrovTangLinearIndependentWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/transcendence-irrationality/index.html#cdt-linear-independent).

## Hermite–Lindemann theorem

If $\alpha$ is a nonzero complex number that is algebraic over
$\mathbb{Q}$, then $e^{\alpha}$ is transcendental over $\mathbb{Q}$.

## Sources

- C. Hermite, Sur la fonction exponentielle, C. R. Acad. Sci. Paris 77 (1873) for e; F. von Lindemann, Über die Zahl π, Math. Ann. 20 (1882) 213–225 extension to π; textbook in Baker, Transcendental Number Theory

Formalized by `MathlibExt.NumberTheory.LindemannWanted.hermite_lindemann`, a theorem declared in [MathlibExt/NumberTheory/Lindemann.lean, line 1494](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Lindemann.lean#L1494). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/transcendence-irrationality/index.html#hermite-lindemann).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Transcendence and irrationality](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/transcendence-irrationality/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/diophantine-approximation/transcendence-irrationality)
