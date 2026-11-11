---
declaration: theorem
origin: cited
lean: TauCeti.projectiveExtEuler_isPerfPair_iff
statement: formalized
proof: formalized
---

# The Euler form is perfect exactly for absolutely simple simples

it identifies either
Grothendieck group with the integral dual of the other if and only if `dim_k End_A(Sᵢ) = 1` for
every `i`. Otherwise the coordinate functional of `[Sᵢ]` is not of the form `χ(x, -)`, since
every value `χ(x, [Sᵢ])` is divisible by `dim_k End_A(Sᵢ)`.

```lean
TauCeti.projectiveExtEuler_isPerfPair_iff.{u, v, u_1} {k : Type u_1} [Field k] {A : Type u} [Ring A]
  [Algebra k A] [Module.Finite k A] [IsArtinianRing A] {I : Type v}
  (P : I → (TauCeti.finiteProjectiveModules A).FullSubcategory) (S : I → FGModuleCat A)
  [hS : ∀ (i : I), IsSimpleModule A ↑(S i)]
  (hind : ∀ (i : I), TauCeti.IsIndecomposableModule A ↑(P i).obj)
  (hPnoniso : Pairwise fun i j => IsEmpty (↑(P i).obj ≃ₗ[A] ↑(P j).obj))
  (hPexhaustive : TauCeti.IsExhaustiveIndecomposableProjectiveFamily P)
  (hSnoniso : Pairwise fun i j => IsEmpty (↑(S i) ≃ₗ[A] ↑(S j)))
  (hSexhaustive : TauCeti.IsExhaustiveSimpleFamily S) {f : (i : I) → ↑(P i).obj →ₗ[A] ↑(S i)}
  (hf : ∀ (i : I), TauCeti.IsProjectiveCover (f i)) [Finite I] :
  (TauCeti.projectiveExtEuler k A).IsPerfPair ↔
    ∀ (i : I), Module.finrank k (Module.End A ↑(S i)) = 1
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The dual Noether isomorphism](../../../category-theory/exact/the-dual-noether-isomorphism.md)
- [The Krull-Schmidt theorem](../../../ring-theory/part-01/krull-schmidt/the-krull-schmidt-theorem.md)
- [The Noether isomorphism for exact categories](../../../category-theory/exact/the-noether-isomorphism-for-exact-categories.md)
- [Schur's lemma, vanishing form](../../../ring-theory/part-01/semisimple/schurs-lemma-vanishing-form.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.projectiveExtEuler_isPerfPair_iff`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/GrothendieckGroup/EulerDuality.html#TauCeti.projectiveExtEuler_isPerfPair_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.projectiveExtEuler_isPerfPair_iff`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/GrothendieckGroup/EulerDuality.html#TauCeti.projectiveExtEuler_isPerfPair_iff)
- [Source of `TauCeti.projectiveExtEuler_isPerfPair_iff` in TauCeti/RepresentationTheory/GrothendieckGroup/EulerDuality.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RepresentationTheory/GrothendieckGroup/EulerDuality.lean#L232)
- [Tau Ceti roadmap status: Grothendieck groups, Cartan maps, and Euler forms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/GrothendieckEulerForms/STATUS.md)
