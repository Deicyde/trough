---
declaration: theorem
origin: cited
lean: TauCeti.dominates_of_asAlgebraHom_columnAntisymmetrizer_ne_zero, TauCeti.YoungTableau.dominates_of_asAlgebraHom_columnAntisymmetrizer_apply_ne_zero
statement: formalized
proof: formalized
---

# James's dominance lemma

If the column antisymmetrizer of a `lam`-tableau `t` does not
annihilate the `μ`-tabloid `q`, then the shape of `t` dominates `μ`.

This is the statement the classification of the Specht modules consumes: a homomorphism
`M^{lam} → M^μ` that does not kill the polytabloid `b_t · {t}` carries it to a combination of the
vectors `b_t · q`, so one of those is nonzero and the shape of `t` dominates `μ`.

```lean
TauCeti.dominates_of_asAlgebraHom_columnAntisymmetrizer_ne_zero {lam : YoungDiagram}
  (t : TauCeti.YoungTableau lam) (μ : lam.card.Partition)
  (q : Equiv.Perm (Fin lam.card) ⧸ TauCeti.youngSubgroup μ)
  (h :
    ((TauCeti.permutationModule μ).ρ.asAlgebraHom t.columnAntisymmetrizer)
        (MonoidAlgebra.single q 1) ≠
      0) :
  (TauCeti.shapePartition lam).Dominates μ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.dominates_of_asAlgebraHom_columnAntisymmetrizer_ne_zero`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Symmetric/Dominance.html#TauCeti.dominates_of_asAlgebraHom_columnAntisymmetrizer_ne_zero).

## Other forms

**James's dominance lemma for an arbitrary vector.** Formalized in Tau Ceti as [`TauCeti.YoungTableau.dominates_of_asAlgebraHom_columnAntisymmetrizer_apply_ne_zero`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Symmetric/Dominance.html#TauCeti.YoungTableau.dominates_of_asAlgebraHom_columnAntisymmetrizer_apply_ne_zero).

```lean
TauCeti.YoungTableau.dominates_of_asAlgebraHom_columnAntisymmetrizer_apply_ne_zero
  {lam : YoungDiagram} (t : TauCeti.YoungTableau lam) (μ : lam.card.Partition)
  {x : ↑(TauCeti.permutationModule μ)}
  (hx : ((TauCeti.permutationModule μ).ρ.asAlgebraHom t.columnAntisymmetrizer) x ≠ 0) :
  (TauCeti.shapePartition lam).Dominates μ
```

## Sources

- [Tau Ceti documentation: `TauCeti.dominates_of_asAlgebraHom_columnAntisymmetrizer_ne_zero`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Symmetric/Dominance.html#TauCeti.dominates_of_asAlgebraHom_columnAntisymmetrizer_ne_zero)
- [Source of `TauCeti.dominates_of_asAlgebraHom_columnAntisymmetrizer_ne_zero` in TauCeti/RepresentationTheory/Symmetric/Dominance.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/Symmetric/Dominance.lean#L129)
