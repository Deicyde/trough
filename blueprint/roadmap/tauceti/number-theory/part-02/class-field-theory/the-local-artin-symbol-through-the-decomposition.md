---
declaration: theorem
origin: cited
lean: TauCeti.ClassFieldTheory.infiniteLocalArtinAt_eq_of_decompositionHom
statement: formalized
proof: formalized
---

# The local Artin symbol through the decomposition group

Let `w` be a place of `L` above
`v`, `ι : L_w → K_vᵃˡᵍ` a `K_v`-embedding and `τ ∈ G_{K_v}` a representative of the archimedean
Artin symbol of `x`. If `σ` is in the decomposition group of `w` and acts on `L_w` as `τ` does
through `ι`, then the local Artin symbol of `x` at `v` is the class of `σ`.

```lean
TauCeti.ClassFieldTheory.infiniteLocalArtinAt_eq_of_decompositionHom {K : Type} [Field K] {L : Type}
  [Field L] [Algebra K L] [FiniteDimensional K L] [Normal K L] (v : NumberField.InfinitePlace K)
  (w : NumberField.InfinitePlace L) [w.LiesOver v] {x : v.Completionˣ}
  (τ : Field.absoluteGaloisGroup v.Completion)
  (hτ : ↑τ = (TauCeti.ClassFieldTheory.infiniteArtinAt v) x)
  (ι : w.Completion →ₐ[v.Completion] AlgebraicClosure v.Completion)
  (σ : ↥(MulAction.stabilizer Gal(L/K) w))
  (hσ : ∀ (y : w.Completion), ι (((v.decompositionHom w) σ) y) = τ.toRingEquiv (ι y)) :
  (TauCeti.ClassFieldTheory.infiniteLocalArtinAt K L v) x = Abelianization.of ↑σ
```

## Depends on

- [Tate's theorem for a class formation, in every integer degree](../../part-01/class-field-theory/tates-theorem-for-a-class-formation-in-every-int.md)

## Proof depends on

- [Corestriction through Shapiro's lemma](../../../representation-theory/homological/corestriction-through-shapiros-lemma.md)
- [Restriction through Shapiro's lemma](../../../representation-theory/homological/restriction-through-shapiros-lemma.md)
- [Shapiro's isomorphism on an adjunct](../../../representation-theory/homological/shapiros-isomorphism-on-an-adjunct.md)
- [Tate's theorem](../../../representation-theory/homological/tates-theorem.md)
- [TauCeti.ClassFieldTheory.tateTheorem](../../part-01/class-field-theory/tauceti-classfieldtheory-tatetheorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ClassFieldTheory.infiniteLocalArtinAt_eq_of_decompositionHom`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Global/LocalArtin/InfinitePlace.html#TauCeti.ClassFieldTheory.infiniteLocalArtinAt_eq_of_decompositionHom).

## Sources

- [Tau Ceti documentation: `TauCeti.ClassFieldTheory.infiniteLocalArtinAt_eq_of_decompositionHom`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Global/LocalArtin/InfinitePlace.html#TauCeti.ClassFieldTheory.infiniteLocalArtinAt_eq_of_decompositionHom)
- [Source of `TauCeti.ClassFieldTheory.infiniteLocalArtinAt_eq_of_decompositionHom` in TauCeti/NumberTheory/ClassFieldTheory/Global/LocalArtin/InfinitePlace.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/ClassFieldTheory/Global/LocalArtin/InfinitePlace.lean#L156)
