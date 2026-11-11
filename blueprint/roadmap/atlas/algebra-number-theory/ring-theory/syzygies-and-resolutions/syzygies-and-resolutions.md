---
declaration: section
origin: cited
lean: MathlibExt.RingTheory.Polynomial.HilbertSyzygyWanted.hilbert_syzygy
statement: formalized
proof: formalized
---

# Syzygies and free resolutions: its own results

1 result, proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/syzygies-and-resolutions/index.html).

Free resolutions of modules over polynomial rings, Hilbert's syzygy theorem, and graded Betti numbers and Poincaré series of multigraded modules.

## Hilbert's syzygy theorem

Let $k$ be a field, let $n$ be a natural number, and let $M$ be a
finitely generated module over the polynomial ring $k[X_1, \dots, X_n]$ in $n$ variables. Then
$M$ has projective dimension at most $n$ in the category of $k[X_1, \dots, X_n]$-modules.

## Sources

- D. Hilbert, Math. Ann. 36 (1890) 473–534 finite free resolution length ≤n; Lang, Algebra; Lean states field case `k[X₁, …, Xₙ]` with `HasProjectiveDimensionLE n` and n=0 field case.

Formalized by `MathlibExt.RingTheory.Polynomial.HilbertSyzygyWanted.hilbert_syzygy`, a theorem declared in [MathlibExt/RingTheory/Polynomial/HilbertSyzygy.lean, line 525](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/Polynomial/HilbertSyzygy.lean#L525). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/syzygies-and-resolutions/index.html#hilbert-syzygy).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Syzygies and free resolutions](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/syzygies-and-resolutions/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/RingTheory/syzygies-and-resolutions)
