---
declaration: def
origin: cited
lean: TauCeti.Huber.Pair.uniformCompletedTensor
statement: formalized
---

# The uniform completed tensor product `(B, B⁺) ⊗̂ᵘ_A (C, C⁺)` of Huber pairs

the
uniformization of the completed tensor product `(B, B⁺) ⊗̂_A (C, C⁺)` (Kedlaya–Liu, the sentence
before Definition 2.8.13). Its ring is a complete Hausdorff uniform Tate ring, and its plus ring
is the closure of the image of the plus ring of the completed tensor product
(`TauCeti.Huber.Pair.uniformCompletedTensor.plus_eq`).

```lean
TauCeti.Huber.Pair.uniformCompletedTensor.{u_1, u_2, u_3} (A : Type u_1) {B : Type u_2}
  {C : Type u_3} [CommRing A] [CommRing B] [CommRing C] [Algebra A B] [Algebra A C]
  [TopologicalSpace A] [TopologicalSpace B] [TopologicalSpace C] [IsTopologicalRing A]
  [IsTopologicalRing B] [IsTopologicalRing C] [TauCeti.Huber.IsHuberRing B]
  [TauCeti.Huber.IsHuberRing C] [TauCeti.Huber.IsAdicHom (algebraMap A B)]
  [TauCeti.Huber.IsAdicHom (algebraMap A C)]
  [TauCeti.Huber.IsTateRing (TauCeti.Huber.CompletedTensor A B C)] (S : TauCeti.Huber.Pair B)
  (T : TauCeti.Huber.Pair C) :
  TauCeti.Huber.Pair (TauCeti.Huber.Uniformization (TauCeti.Huber.CompletedTensor A B C))
```

## Depends on

- [The completed tensor product `(B, B⁺) ⊗̂_A (C, C⁺)` of Huber pairs along adic structure maps](the-completed-tensor-product-b-b-a-c-c-of-huber.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Huber.Pair.uniformCompletedTensor`](https://taucetiproject.org/docs/TauCeti/RingTheory/Huber/TensorProduct/Uniform.html#TauCeti.Huber.Pair.uniformCompletedTensor).

## Sources

- [Tau Ceti documentation: `TauCeti.Huber.Pair.uniformCompletedTensor`](https://taucetiproject.org/docs/TauCeti/RingTheory/Huber/TensorProduct/Uniform.html#TauCeti.Huber.Pair.uniformCompletedTensor)
- [Source of `TauCeti.Huber.Pair.uniformCompletedTensor` in TauCeti/RingTheory/Huber/TensorProduct/Uniform.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/Huber/TensorProduct/Uniform.lean#L71)
- [Tau Ceti roadmap status: Foundations of adic spaces, part II — morphisms and analytification](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AdicSpacesPartII/STATUS.md)
