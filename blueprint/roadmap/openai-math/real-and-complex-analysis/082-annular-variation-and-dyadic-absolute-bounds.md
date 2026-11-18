---
declaration: section
origin: cited
lean: OAI.TriangularHilbert.main_estimate
statement: formalized
proof: formalized
---

# 082. Annular variation and dyadic absolute bounds for the triangular Hilbert transform

3 manuscripts and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves maximal and annular *r*-variation bounds, for every *r* > 2, from complex $L^3(\mathbb R^2)\times L^3(\mathbb R^2)$ to $L^{3/2}(\mathbb R^2)$. The maximal estimate controls both hard truncation endpoints and gives almost-everywhere and norm convergence. Pairing with a third input settles the triangular Hilbert transform estimate at the symmetric $L^3\times L^3\times L^3$ point.

## Annular variation of the triangular Hilbert transform at the symmetric point

We prove the annular *r*-variation estimate for the triangular Hilbert transform from complex $L^3\times L^3$ to $L^{3/2}$ for every *r* > 2. The partitions may depend on the output point and range over all positive scales. The estimate yields the two-endpoint maximal bound and joint almost-everywhere and norm principal values, and resolves the symmetric scalar triangular Hilbert transform problem.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Annular-variation-of-the-triangular-Hilbert-transform-at-the-symmetric-point-October-5-2026/annular-variation.pdf).

## An L³ bound for the dyadic triangular Hilbert form

We prove a uniform $L^3\times L^3\times L^3$ estimate for the dyadic triangular Hilbert form with unrestricted real inputs. The sum of the absolute local contributions over any finite set of scales is bounded by forty times the product of the input norms. In particular, the bound allows coefficients of modulus at most one to vary independently among admissible interval triples.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/An-L3-bound-for-the-dyadic-triangular-Hilbert-form-October-5-2026/dyadic-triangular-hilbert.pdf).

## The maximal triangular Hilbert transform at the symmetric point

For arbitrary complex inputs in $L^3(\mathbb R^2)$, we prove the pointwise maximal $L^3\times L^3\to L^{3/2}$ estimate for the triangular Hilbert transform, with the supremum over both hard truncation endpoints. The estimate yields joint almost-everywhere and $L^{3/2}$ convergence as the lower endpoint tends to zero and the upper endpoint tends to infinity. This also proves the conjectured scalar estimate at the symmetric point.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/The-maximal-triangular-Hilbert-transform-at-the-symmetric-point-September-24-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalized result proves the symmetric maximal estimate for the triangular Hilbert transform: for arbitrary complex $F,G\in L^3(\mathbb R^2)$, the $L^{3/2}$ norm of the supremum over all finite hard-truncation intervals is at most $C\|F\|_3\|G\|_3$ for one absolute constant $C$. It also establishes a common full-measure set on which the truncated integrals are defined and almost-everywhere measurability of the maximal output.

## Lean: Maximal triangular Hilbert transform bound

```lean
theorem main_estimate : MainEstimate
```

Stated in [TriangularHilbert.lean, line 50](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/TriangularHilbert.lean#L50). Proved in [lean/OAI/Analysis/TriangularHilbert/Main.lean, line 38](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/TriangularHilbert/Main.lean#L38). formalization.yaml lists it as one of the repository's main results.

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/082.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/082.md)
