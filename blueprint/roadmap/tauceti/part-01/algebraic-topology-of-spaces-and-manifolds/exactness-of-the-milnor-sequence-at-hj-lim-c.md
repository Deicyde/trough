---
declaration: theorem
origin: cited
lean: TauCeti.ComplexTower.exact_limOneToHomology_homologyToLim
statement: formalized
proof: formalized
---

# Exactness of the Milnor sequence at `Hⱼ(lim C)`

For a tower whose shift is surjective
in every degree, the image of `lim¹ Hᵢ(Cₙ) → Hⱼ(lim C)` is the kernel of
`Hⱼ(lim C) → lim Hⱼ(Cₙ)`.

```lean
TauCeti.ComplexTower.exact_limOneToHomology_homologyToLim.{v, u, w} {R : Type u} [Ring R]
  {ι : Type w} {c : ComplexShape ι} {C : TauCeti.ComplexTower R c}
  (hC : ∀ (i : ι), Function.Surjective ⇑(C.term i).shift) {i j : ι} (hij : c.Rel i j) :
  Function.Exact ⇑(TauCeti.ComplexTower.limOneToHomology hC hij) ⇑(C.homologyToLim j)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.ComplexTower.exact_limOneToHomology_homologyToLim`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/ModuleCat/Tower/Milnor/Basic.html#TauCeti.ComplexTower.exact_limOneToHomology_homologyToLim).

## Sources

- [Tau Ceti documentation: `TauCeti.ComplexTower.exact_limOneToHomology_homologyToLim`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/ModuleCat/Tower/Milnor/Basic.html#TauCeti.ComplexTower.exact_limOneToHomology_homologyToLim)
- [Source of `TauCeti.ComplexTower.exact_limOneToHomology_homologyToLim` in TauCeti/Algebra/Category/ModuleCat/Tower/Milnor/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Category/ModuleCat/Tower/Milnor/Basic.lean#L540)
- [Tau Ceti roadmap status: Algebraic topology of spaces and manifolds](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AlgebraicTopology/STATUS.md)
