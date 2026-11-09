---
declaration: theorem
origin: cited
lean: FDRep.clifford_restrict_dvd_finrank
statement: formalized
proof: formalized
---

# The divisibilities in Clifford's theorem

For an irreducible constituent `V` of the
restriction of an irreducible `W` to a normal subgroup, both the index of the inertia group of `V`
and the dimension of `V` divide the dimension of `W`; the index divides `[G : N]`, and it divides
the quotient `dim W / (e * dim V)` that the dimension identity leaves.

The decomposition `Res_N W ≅ V.cliffordSum e` is carried along from
`FDRep.clifford_restrict_finrank`, so that `V` is exhibited as a constituent of the restriction and
the divisibilities are read as statements about that constituent rather than about some unrelated
irreducible representation of `N`.

This is the form in which the dimension identity of `FDRep.clifford_restrict_finrank` is used.  The
number of distinct conjugates occurring in the restriction is `[G : inertia V]`, and it is
constrained from two sides at once: by the degree of `W`, through the dimension identity, and by
the index of `N`, through `TauCeti.le_inertia`.  Neither constraint mentions the multiplicity `e`,
which the last divisibility divides out instead: `dim W / (e * dim V)` counts the distinct
conjugates.

```lean
FDRep.clifford_restrict_dvd_finrank.{u, v} {k : Type u} {G : Type v} [Field k] [Group G]
  {N : Subgroup G} [N.Normal] [IsAlgClosed k] (W : FDRep k G) [CategoryTheory.Simple W] :
  ∃ V,
    ∃ (_ : CategoryTheory.Simple V) (hfinite : Finite (G ⧸ TauCeti.inertia V)),
      have x := hfinite;
      ∃ e,
        e ≠ 0 ∧
          Nonempty (N.resFDRep W ≅ V.cliffordSum e) ∧
            (TauCeti.inertia V).index ∣ Module.finrank k ↑W.V ∧
              Module.finrank k ↑V.V ∣ Module.finrank k ↑W.V ∧
                (TauCeti.inertia V).index ∣ N.index ∧
                  (TauCeti.inertia V).index ∣ Module.finrank k ↑W.V / (e * Module.finrank k ↑V.V)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Clifford's theorem, dimension form](cliffords-theorem-dimension-form.md)

## Lean

Formalized in Tau Ceti as [`FDRep.clifford_restrict_dvd_finrank`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Induction/Clifford/Dimension.html#FDRep.clifford_restrict_dvd_finrank).

## Sources

- [Tau Ceti documentation: `FDRep.clifford_restrict_dvd_finrank`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Induction/Clifford/Dimension.html#FDRep.clifford_restrict_dvd_finrank)
- [Source of `FDRep.clifford_restrict_dvd_finrank` in TauCeti/RepresentationTheory/Induction/Clifford/Dimension.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/Induction/Clifford/Dimension.lean#L97)
