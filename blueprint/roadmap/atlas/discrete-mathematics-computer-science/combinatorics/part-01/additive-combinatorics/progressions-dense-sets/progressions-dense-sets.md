---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.Additive.SzemerediWanted.szemeredi
statement: formalized
proof: formalized
---

# Arithmetic progressions in dense sets: its own results

1 result, proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/index.html).

Density versions: Szemerédi's and Roth's theorems and Roth-number bounds, Sárközy's theorem, cap sets, counts of three-term progressions, progressions in complements and in walks, arithmetic progression API, and polynomial triangle removal in vector spaces.

## Szemerédi's theorem

For every natural number $k \ge 1$ and every real number $\delta > 0$
there is a natural number $N$ such that for every $n \ge N$, every set
$A \subseteq \{0, 1, \dots, n - 1\}$ with $\delta n \le |A|$ contains an arithmetic progression
of length $k$: there are natural numbers $a$ and $d > 0$ with $a + i d \in A$ for all $i < k$.

Proof: We derive the result from the density Hales–Jewett theorem by averaging coordinate-sum
translates and mapping combinatorial lines to arithmetic progressions.

## Sources

- E. Szemerédi, Acta Arith. 27 (1975); Lean states finitary density form equivalent to infinitary positive upper density k-AP existence.

Formalized by `MathlibExt.Combinatorics.Additive.SzemerediWanted.szemeredi`, a theorem declared in [MathlibExt/Combinatorics/Additive/Szemeredi.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Additive/Szemeredi.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/index.html#szemeredi).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Arithmetic progressions in dense sets](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets)
