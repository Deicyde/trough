---
declaration: def
origin: cited
lean: TauCeti.presentedProP.oneRelatorAbelianizationEquiv, TauCeti.IsDemushkin.nonempty_continuousMulEquiv_topologicalAbelianization
statement: formalized
---

# The abelianization structure theorem for one-relator pro-`p` groups

Let
`G = presentedProP p X {r}` be the pro-`p` group on a finite type `X` with the single relator `r`,
and write the exponent vector of `r` as `exponentSum r = q • w` with `w x₀ = 1`. Then

`G^{ab} ≃ₜ* ℤ_p^{X ∖ {x₀}} × ℤ_p ⧸ q ℤ_p`

as topological groups, the isomorphism sending the class of the generator at `x ≠ x₀` to the
coordinate vector at `x` and the class of the generator at `x₀` to `(-w, 1)`. When `q ≠ 0` the
factor `ℤ_p ⧸ q ℤ_p` is finite cyclic and is the torsion subgroup of `G^{ab}`; when `q = 0` it is
`ℤ_p` and `G^{ab} ≅ ℤ_p^X` is torsion-free.

```lean
TauCeti.presentedProP.oneRelatorAbelianizationEquiv.{u} {p : ℕ} [Fact (Nat.Prime p)] {X : Type u}
  (r : TauCeti.freeProP p X) (x₀ : X) (w : X → ℤ_[p]) (hw : w x₀ = 1) (q : ℤ_[p])
  (hr : Multiplicative.toAdd ((TauCeti.freeProP.exponentSum p X) r) = q • w) [Finite X] :
  TopologicalAbelianization (TauCeti.presentedProP p X {r}) ≃ₜ*
    Multiplicative (({ x // x ≠ x₀ } → ℤ_[p]) × ℤ_[p] ⧸ Ideal.span {q})
```

## Depends on

- [The Demushkin predicate](../../profinite-and-pro-p-groups/the-demushkin-predicate.md)

## Proof depends on

- [Burnside's basis theorem, cardinal form](burnsides-basis-theorem-cardinal-form.md)
- [The first isomorphism theorem for a surjective strict homomorphism of topological groups](the-first-isomorphism-theorem-for-a-surjective-s.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.presentedProP.oneRelatorAbelianizationEquiv`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Presentation/Abelianization.html#TauCeti.presentedProP.oneRelatorAbelianizationEquiv).

## Other forms

**The abelianization structure theorem for Demushkin groups (Labute, p. 106).** Formalized in Tau Ceti as [`TauCeti.IsDemushkin.nonempty_continuousMulEquiv_topologicalAbelianization`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/QInvariant.html#TauCeti.IsDemushkin.nonempty_continuousMulEquiv_topologicalAbelianization).

```lean
TauCeti.IsDemushkin.nonempty_continuousMulEquiv_topologicalAbelianization.{u} {p : ℕ}
  [Fact (Nat.Prime p)] {G : Type u} [Group G] [TopologicalSpace G] [IsTopologicalGroup G]
  (hG : TauCeti.IsDemushkin p G) [CompactSpace G] [TotallyDisconnectedSpace G] :
  Nonempty
    (TopologicalAbelianization G ≃ₜ*
      Multiplicative
        ((Fin (TauCeti.demushkinRank hG - 1) → ℤ_[p]) ×
          ℤ_[p] ⧸ Ideal.span {↑(TauCeti.demushkinQ hG)}))
```

## Sources

- [Tau Ceti documentation: `TauCeti.presentedProP.oneRelatorAbelianizationEquiv`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Presentation/Abelianization.html#TauCeti.presentedProP.oneRelatorAbelianizationEquiv)
- [Source of `TauCeti.presentedProP.oneRelatorAbelianizationEquiv` in TauCeti/Topology/Algebra/Group/Profinite/Presentation/Abelianization.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/Group/Profinite/Presentation/Abelianization.lean#L319)
