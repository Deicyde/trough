---
declaration: theorem
origin: cited
lean: TauCeti.AlgebraicGeometry.Scheme.isNisnevichCovering_iff_henselization
statement: formalized
proof: formalized
---

# The henselization criterion for Nisnevich coverings

A family of étale morphisms
`{fᵢ : Xᵢ ⟶ S}` is a Nisnevich covering if and only if, for every point `s` of `S`, the morphism
`Spec 𝒪ʰ_{S,s} ⟶ S` lifts to some `Xᵢ`; equivalently, the base change of some `fᵢ` to
`Spec 𝒪ʰ_{S,s}` has a section. Morel–Voevodsky, §3.1, Proposition 1.1.

```lean
TauCeti.AlgebraicGeometry.Scheme.isNisnevichCovering_iff_henselization.{u, u_1}
  {S : AlgebraicGeometry.Scheme} {ι : Type u_1} {X : ι → AlgebraicGeometry.Scheme}
  (f : (i : ι) → X i ⟶ S) :
  TauCeti.AlgebraicGeometry.Scheme.IsNisnevichCovering f ↔
    (∀ (i : ι), AlgebraicGeometry.Etale (f i)) ∧
      ∀ (s : ↥S), ∃ i t, CategoryTheory.CategoryStruct.comp t (f i) = S.fromSpecHenselization s
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Cayley–Hamilton in size two](../../linear-algebra/matrix/cayley-hamilton-in-size-two.md)
- [Nakayama's lemma for an idempotent](../../ring-theory/part-02/other-results/part-02/nakayamas-lemma-for-an-idempotent.md)
- [Zariski's main theorem, global form](../../ring-theory/part-02/other-results/part-03/zariskis-main-theorem-global-form.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.Scheme.isNisnevichCovering_iff_henselization`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Sites/Nisnevich/Henselization.html#TauCeti.AlgebraicGeometry.Scheme.isNisnevichCovering_iff_henselization).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.Scheme.isNisnevichCovering_iff_henselization`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Sites/Nisnevich/Henselization.html#TauCeti.AlgebraicGeometry.Scheme.isNisnevichCovering_iff_henselization)
- [Source of `TauCeti.AlgebraicGeometry.Scheme.isNisnevichCovering_iff_henselization` in TauCeti/AlgebraicGeometry/Sites/Nisnevich/Henselization.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/Sites/Nisnevich/Henselization.lean#L50)
- [Tau Ceti roadmap status: Scheme, stack, cohomology and intersection foundations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SchemeAndStackFoundations/STATUS.md)
