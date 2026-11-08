---
declaration: theorem
origin: cited
lean: TauCeti.galoisEvens2_kummerClass_eq_cup_add_cup
statement: formalized
proof: formalized
---

# Serre's formula for the Evens norm of a Kummer class (Serre, Théorème 1′ at `n = 2`)

for an orthogonal basis `y` of the twisted trace form `Tr_*⟨a⟩ : z ↦ Tr (a z²)` whose values
`w_j = Tr (a y_j²)` are units,

```text
N^{Ev}((a)) = (w₁) ∪ (w₀) + (2) ∪ (d),
```

where `d` is the square of a generator `x` of `L = K(x)`. Since `(w₀) ∪ (w₁)` is the second
Stiefel–Whitney class of `⟨w₀, w₁⟩ ≅ Tr_*⟨a⟩`, this is `w₂(Tr_*⟨a⟩) = N^{Ev}((a)) + (2) ∪ (d)`.

```lean
TauCeti.galoisEvens2_kummerClass_eq_cup_add_cup.{u} {K : Type u} [Field K] [Invertible 2]
  {L : Type u} [Field L] [Algebra K L] [FiniteDimensional K L] [Algebra.IsSeparable K L]
  [Invertible 2] (σ : L →ₐ[K] SeparableClosure K) (hdeg : Module.finrank K L = 2) (d : Kˣ) {x : L}
  (hx : x ∉ Set.range ⇑(algebraMap K L)) (hx2 : x ^ 2 = (algebraMap K L) ↑d) (a : Lˣ)
  (y : Fin 2 → L) (hy : (Algebra.trace K L) (↑a * y 0 * y 1) = 0) (w : Fin 2 → Kˣ)
  (hw : ∀ (i : Fin 2), ↑(w i) = (Algebra.trace K L) (↑a * y i ^ 2)) :
  TauCeti.galoisEvens K L σ hdeg (TauCeti.kummerClass a) =
    (((TauCeti.trivialF2TopPairing (TauCeti.AbsoluteGaloisGroup K)).cup 1 1)
          (TauCeti.kummerClass (w 1)))
        (TauCeti.kummerClass (w 0)) +
      (((TauCeti.trivialF2TopPairing (TauCeti.AbsoluteGaloisGroup K)).cup 1 1)
          (TauCeti.kummerClass (unitOfInvertible 2)))
        (TauCeti.kummerClass d)
```

## Depends on

- [The index-two degree-one Evens norm `Nᴱᵛ : H¹(U, 𝔽₂) → H²(G, 𝔽₂)` for an open subgroup `U` of index two](../../representation-theory/continuous-cohomology-of-profinite-groups/the-index-two-degree-one-evens-norm-nev-h1-u-f2.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.galoisEvens2_kummerClass_eq_cup_add_cup`](https://taucetiproject.org/docs/TauCeti/FieldTheory/QuadraticForm/StiefelWhitney/Evens/Kummer/Value.html#TauCeti.galoisEvens2_kummerClass_eq_cup_add_cup).

## Sources

- [Tau Ceti documentation: `TauCeti.galoisEvens2_kummerClass_eq_cup_add_cup`](https://taucetiproject.org/docs/TauCeti/FieldTheory/QuadraticForm/StiefelWhitney/Evens/Kummer/Value.html#TauCeti.galoisEvens2_kummerClass_eq_cup_add_cup)
- [Source of `TauCeti.galoisEvens2_kummerClass_eq_cup_add_cup` in TauCeti/FieldTheory/QuadraticForm/StiefelWhitney/Evens/Kummer/Value.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/FieldTheory/QuadraticForm/StiefelWhitney/Evens/Kummer/Value.lean#L67)
