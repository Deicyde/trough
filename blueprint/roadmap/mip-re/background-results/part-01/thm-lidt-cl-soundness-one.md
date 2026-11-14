---
declaration: theorem
origin: cited
lean: MIPRE.LIDT.Adapter.clSoundness_ldc_one, MIPRE.LIDT.Adapter.clSoundness_ldc_one_deltaCL
statement: formalized
proof: formalized
---

# Quantum soundness of the seeded CL test, one codeword

Let $m,d\geq1$, $m\mid q$ and $\varepsilon\geq0$. Every projective strategy passing the seeded CL test at $(q,m,d,1)$ with probability at least $1-\varepsilon$ admits projective measurements $G^\textsc{A},G^\textsc{B}$ on the respective players' spaces with outcomes polynomials of individual degree at most $d$, such that A's point measurement is consistent with $G^\textsc{B}$ evaluated at the point on average over uniform $u\in\mathbb{F}_q^m$, $G^\textsc{A}$ evaluated at the point is consistent with B's point measurement, and $G^\textsc{A}$ and $G^\textsc{B}$ are consistent with each other, all with error at most $\delta_{\mathrm{CL}}(\varepsilon,q,m,d,1)=a(dm)^a(\varepsilon^b+q^{-b}+2^{-bmd})$ for the constants of Lemma [The parameter choice](lem-lidt-cl-adapter-params.md).

## Depends on

- [Seeded CL low individual degree test](def-lidt-cl.md)
- [Inconsistency](../../foundations/part-02/def-inconsistency.md)
- [Quantum soundness of the canonical-line low individual degree test](thm-lidt-soundness.md)
- [The adapter's two maps, and acceptance](lem-lidt-cl-adapter-maps.md)
- [The adapter's cost in the question distributions](lem-lidt-cl-adapter-weights.md)
- [The parameter choice](lem-lidt-cl-adapter-params.md)

## Proof depends on

- [Bipartite model](../../downstream-results/part-02/def-bipartite-model.md)

## Proof

Lemma [The adapter's two maps, and acceptance](lem-lidt-cl-adapter-maps.md) gives, for each family member, a strategy for the canonical-line test built from the seeded one by reindexing the questions and coarse-graining the answers — same spaces, same state, so projectivity and the dimensions are untouched. Lemma [The adapter's cost in the question distributions](lem-lidt-cl-adapter-weights.md) bounds the failure of the adapted strategy by $3m$ times the failure of the original, on average over the family, so some member achieves it; that is the choice of seed the seeding makes necessary. Theorem [Quantum soundness of the canonical-line low individual degree test](thm-lidt-soundness.md) applies to it at the $k$ of Lemma [The parameter choice](lem-lidt-cl-adapter-params.md), and that lemma converts its error.

The three conclusions come back through the coordinate reversal. It relabels the questions by a bijection that preserves the uniform distribution, and the outcomes by the same reversal of a polynomial's exponent vectors — a bijection of the polynomials of individual degree at most $d$, the bound being symmetric in the variables — under which evaluation at $u$ becomes evaluation at $\rho u$. Consistency is invariant under both.

## Lean

Formalized as [`MIPRE.LIDT.Adapter.clSoundness_ldc_one`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Adapter.clSoundness_ldc_one), [`MIPRE.LIDT.Adapter.clSoundness_ldc_one_deltaCL`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Adapter.clSoundness_ldc_one_deltaCL).

## Sources

- [MIP* = RE blueprint: content/03_background_results.tex, line 920](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L920)
