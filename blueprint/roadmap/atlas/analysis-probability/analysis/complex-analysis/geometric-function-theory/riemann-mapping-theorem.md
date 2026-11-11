---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Complex.RiemannMappingWanted.riemannMapping_normalized, MathlibExt.Analysis.Complex.InjectiveDiskMapExtremalDerivWanted.unitDisk, MathlibExt.Analysis.Complex.InjectiveDiskMapExtremalDerivWanted.AdmissibleFamily, MathlibExt.Analysis.Complex.InjectiveDiskMapExtremalDerivWanted.exists_mem_admissibleFamily_norm_deriv_eq_sSup
statement: formalized
---

# Riemann mapping theorem

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/riemann-mapping-theorem/index.html).

## Riemann mapping theorem

Let $U$ be a simply connected open subset of $\mathbb{C}$ with
$U \ne \mathbb{C}$, and let $z_0 \in U$. Then there is a function $f : \mathbb{C} \to \mathbb{C}$,
holomorphic on $U$, that maps $U$ bijectively onto the open unit disc $\{w : |w| < 1\}$, with
$f(z_0) = 0$ and $f'(z_0)$ a positive real number. It is unique on $U$: every function
$g : \mathbb{C} \to \mathbb{C}$ with the same four properties agrees with $f$ at every point of $U$.

## Sources

- same as Riemann mapping; B. Riemann thesis 1851; W. F. Osgood Trans. Amer. Math. Soc. 1 (1900), 310–314, DOI 10.2307/1986285; C. Carathéodory Math. Ann. 72 (1912), 107–144, DOI 10.1007/BF01456892; Ahlfors; Lean adds f z₀=0 positive real derivative via im=0 re>0 and EqOn uniqueness on U.

Formalized by `MathlibExt.Analysis.Complex.RiemannMappingWanted.riemannMapping_normalized`, a theorem declared in [MathlibExt/Analysis/Complex/RiemannMapping.lean, line 1250](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/RiemannMapping.lean#L1250). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/riemann-mapping-theorem/index.html#riemann-mapping-normalized).

## Open unit disc

The open unit disc is the set of complex numbers $z$ with $|z| < 1$, the
open ball of radius $1$ about $0$ in $\mathbb{C}$.

Formalized by `MathlibExt.Analysis.Complex.InjectiveDiskMapExtremalDerivWanted.unitDisk`, an abbreviation declared in [WantedExt/Analysis/Complex/InjectiveDiskMapExtremalDerivWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Complex/InjectiveDiskMapExtremalDerivWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/riemann-mapping-theorem/index.html#unit-disk).

## Admissible maps into the unit disc

For a set $\Omega \subseteq \mathbb{C}$, the
admissible family of $\Omega$ is the set of functions $f : \mathbb{C} \to \mathbb{C}$ that are
complex differentiable on $\Omega$, injective on $\Omega$, satisfy $f(0) = 0$, and map $\Omega$
into the open unit disc $\{z \in \mathbb{C} : |z| < 1\}$.

Formalized by `MathlibExt.Analysis.Complex.InjectiveDiskMapExtremalDerivWanted.AdmissibleFamily`, a definition declared in [WantedExt/Analysis/Complex/InjectiveDiskMapExtremalDerivWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Complex/InjectiveDiskMapExtremalDerivWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/riemann-mapping-theorem/index.html#admissible-family).

## Existence of an extremal injective map into the unit disc

Let $D$ be the open unit disc
$\{z \in \mathbb{C} : |z| < 1\}$, let $\Omega \subseteq D$ be open and connected with
$0 \in \Omega$, and let $F$ be the family of functions $f$ that are holomorphic and injective on
$\Omega$, map $\Omega$ into $D$, and satisfy $f(0) = 0$. Then some $g \in F$ attains the supremum
of $|f'(0)|$ over $F$:

$$|g'(0)| = \sup_{f \in F} |f'(0)|.$$

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Functions of a complex variable; Geometric function theory), problem `ma_proofbench_l2_22`.

Stated but not proved: `MathlibExt.Analysis.Complex.InjectiveDiskMapExtremalDerivWanted.exists_mem_admissibleFamily_norm_deriv_eq_sSup` is written with `theorem_wanted` in [WantedExt/Analysis/Complex/InjectiveDiskMapExtremalDerivWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Complex/InjectiveDiskMapExtremalDerivWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/riemann-mapping-theorem/index.html#exists-mem-admissible-family-norm-deriv).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Riemann mapping theorem](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/riemann-mapping-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/complex-analysis/geometric-function-theory/riemann-mapping-theorem)
