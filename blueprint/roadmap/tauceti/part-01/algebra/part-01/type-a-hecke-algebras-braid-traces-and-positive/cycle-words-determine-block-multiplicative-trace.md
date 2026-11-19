---
declaration: theorem
origin: cited
lean: TauCeti.InfiniteTypeAHeckeAlgebra.towerTrace_eq_of_cycleChain_values
statement: formalized
proof: formalized
---

# Cycle words determine block-multiplicative traces

Two tracial linear functionals on the
infinite type-A Hecke algebra, both multiplicative on disjoint blocks of strands, are equal as
soon as they agree on every cycle word `ζₘ`.

```lean
TauCeti.InfiniteTypeAHeckeAlgebra.towerTrace_eq_of_cycleChain_values.{u_1} {R : Type u_1}
  [CommRing R] {q : Rˣ} {τ τ' : TauCeti.InfiniteTypeAHeckeAlgebra R q →ₗ[R] R}
  (hτ : ∀ (x y : TauCeti.InfiniteTypeAHeckeAlgebra R q), τ (x * y) = τ (y * x))
  (hτ' : ∀ (x y : TauCeti.InfiniteTypeAHeckeAlgebra R q), τ' (x * y) = τ' (y * x))
  (hτm :
    ∀ {a : ℕ} {x : TauCeti.InfiniteTypeAHeckeAlgebra R q},
      x ∈ TauCeti.InfiniteTypeAHeckeAlgebra.stage R q a →
        ∀ (y : TauCeti.InfiniteTypeAHeckeAlgebra R q),
          τ (x * (TauCeti.InfiniteTypeAHeckeAlgebra.shift R q a) y) = τ x * τ y)
  (hτm' :
    ∀ {a : ℕ} {x : TauCeti.InfiniteTypeAHeckeAlgebra R q},
      x ∈ TauCeti.InfiniteTypeAHeckeAlgebra.stage R q a →
        ∀ (y : TauCeti.InfiniteTypeAHeckeAlgebra R q),
          τ' (x * (TauCeti.InfiniteTypeAHeckeAlgebra.shift R q a) y) = τ' x * τ' y)
  (h :
    ∀ (m : ℕ),
      τ (TauCeti.InfiniteTypeAHeckeAlgebra.cycleWord q m) =
        τ' (TauCeti.InfiniteTypeAHeckeAlgebra.cycleWord q m)) :
  τ = τ'
```

## Depends on

- [TauCeti.InfiniteTypeAHeckeAlgebra](tauceti-infinitetypeaheckealgebra.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.InfiniteTypeAHeckeAlgebra.towerTrace_eq_of_cycleChain_values`](https://taucetiproject.org/docs/TauCeti/Algebra/TypeAHeckeAlgebra/Cocenter/Basic.html#TauCeti.InfiniteTypeAHeckeAlgebra.towerTrace_eq_of_cycleChain_values).

## Sources

- [Tau Ceti documentation: `TauCeti.InfiniteTypeAHeckeAlgebra.towerTrace_eq_of_cycleChain_values`](https://taucetiproject.org/docs/TauCeti/Algebra/TypeAHeckeAlgebra/Cocenter/Basic.html#TauCeti.InfiniteTypeAHeckeAlgebra.towerTrace_eq_of_cycleChain_values)
- [Source of `TauCeti.InfiniteTypeAHeckeAlgebra.towerTrace_eq_of_cycleChain_values` in TauCeti/Algebra/TypeAHeckeAlgebra/Cocenter/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/TypeAHeckeAlgebra/Cocenter/Basic.lean#L664)
- [Tau Ceti roadmap status: Type-A Hecke algebras, braid traces, and positive quotients](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/TypeAHeckeAlgebras/STATUS.md)
