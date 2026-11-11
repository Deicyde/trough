---
declaration: theorem
origin: cited
lean: TauCeti.exists_quiver_admissibleIdeal_morita, TauCeti.IsBasic.exists_surjective_pathAlgebra_isAdmissibleIdeal_ker
statement: formalized
proof: formalized
---

# Gabriel's presentation theorem

Every finite-dimensional algebra `A` over an algebraically
closed field `k` is Morita equivalent to a bound quiver algebra: there are a finite quiver `Q`
and an admissible ideal `I` of the path algebra `kQ` such that `A` is Morita equivalent to
`kQ ⧸ I`. The algebra `kQ ⧸ I` is isomorphic to the basic corner `eAe` of `A`
(`TauCeti.IsSemiperfectRing.exists_isIdempotentElem_full_isBasic_corner`), presented by
`TauCeti.IsBasic.exists_surjective_pathAlgebra_isAdmissibleIdeal_ker`.

```lean
TauCeti.exists_quiver_admissibleIdeal_morita.{u, w} (k : Type w) (A : Type u) [Field k]
  [IsAlgClosed k] [Ring A] [Algebra k A] [FiniteDimensional k A] :
  ∃ Q x,
    ∃ (x_1 : Finite Q) (_ : ∀ (i j : Q), Finite (i ⟶ j)),
      ∃ I,
        ∃ (x_3 : I.IsTwoSided),
          TauCeti.IsAdmissibleIdeal I ∧ IsMoritaEquivalent k A (TauCeti.pathAlgebra k Q ⧸ I)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_quiver_admissibleIdeal_morita`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Quiver/AdmissibleIdeal/Presentation.html#TauCeti.exists_quiver_admissibleIdeal_morita).

## Other forms

**Gabriel's presentation theorem for basic algebras.** Formalized in Tau Ceti as [`TauCeti.IsBasic.exists_surjective_pathAlgebra_isAdmissibleIdeal_ker`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Quiver/AdmissibleIdeal/Presentation.html#TauCeti.IsBasic.exists_surjective_pathAlgebra_isAdmissibleIdeal_ker).

```lean
TauCeti.IsBasic.exists_surjective_pathAlgebra_isAdmissibleIdeal_ker.{u, w} {k : Type w} {A : Type u}
  [Field k] [IsAlgClosed k] [Ring A] [Algebra k A] [FiniteDimensional k A]
  (hA : TauCeti.IsBasic A) :
  ∃ Q x,
    ∃ (x_1 : Finite Q) (_ : ∀ (i j : Q), Finite (i ⟶ j)),
      ∃ F, Function.Surjective ⇑F ∧ TauCeti.IsAdmissibleIdeal (RingHom.ker F.toRingHom)
```

## Sources

- [Tau Ceti documentation: `TauCeti.exists_quiver_admissibleIdeal_morita`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Quiver/AdmissibleIdeal/Presentation.html#TauCeti.exists_quiver_admissibleIdeal_morita)
- [Source of `TauCeti.exists_quiver_admissibleIdeal_morita` in TauCeti/RepresentationTheory/Quiver/AdmissibleIdeal/Presentation.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RepresentationTheory/Quiver/AdmissibleIdeal/Presentation.lean#L224)
