---
declaration: theorem
origin: cited
lean: TauCeti.mem_convexHull_range_comp_perm_iff, TauCeti.mem_convexHull_range_comp_perm_iff_of_antitone
statement: formalized
proof: formalized
---

# Rado's theorem

For antitone `w`, a tuple `x` lies in the convex hull of the permutation
orbit of `w` exactly when `x` is majorized by `w`: the prefix sums of the decreasing
rearrangement of `x` are at most those of `w`, and the total sums agree.

```lean
TauCeti.mem_convexHull_range_comp_perm_iff {n : ℕ} {w x : Fin n → ℝ} (hw : Antitone w) :
  x ∈ (convexHull ℝ) (Set.range fun σ => w ∘ ⇑σ) ↔
    (∀ (k : ℕ), TauCeti.prefixSum k (x ∘ ⇑(Tuple.sortDesc x)) ≤ TauCeti.prefixSum k w) ∧
      ∑ i, x i = ∑ i, w i
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.mem_convexHull_range_comp_perm_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/Convex/PermutationOrbit.html#TauCeti.mem_convexHull_range_comp_perm_iff).

## Other forms

**Rado's theorem for antitone tuples.** Formalized in Tau Ceti as [`TauCeti.mem_convexHull_range_comp_perm_iff_of_antitone`](https://taucetiproject.org/docs/TauCeti/Analysis/Convex/PermutationOrbit.html#TauCeti.mem_convexHull_range_comp_perm_iff_of_antitone).

```lean
TauCeti.mem_convexHull_range_comp_perm_iff_of_antitone {n : ℕ} {w x : Fin n → ℝ} (hw : Antitone w)
  (hx : Antitone x) :
  x ∈ (convexHull ℝ) (Set.range fun σ => w ∘ ⇑σ) ↔
    (∀ (k : ℕ), TauCeti.prefixSum k x ≤ TauCeti.prefixSum k w) ∧ ∑ i, x i = ∑ i, w i
```

## Sources

- [Tau Ceti documentation: `TauCeti.mem_convexHull_range_comp_perm_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/Convex/PermutationOrbit.html#TauCeti.mem_convexHull_range_comp_perm_iff)
- [Source of `TauCeti.mem_convexHull_range_comp_perm_iff` in TauCeti/Analysis/Convex/PermutationOrbit.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Convex/PermutationOrbit.lean#L250)
