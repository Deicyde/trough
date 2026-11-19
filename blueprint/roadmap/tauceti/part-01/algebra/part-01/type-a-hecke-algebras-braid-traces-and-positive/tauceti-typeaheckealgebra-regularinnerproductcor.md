---
declaration: def
origin: cited
lean: TauCeti.TypeAHeckeAlgebra.regularInnerProductCore
statement: formalized
---

# TauCeti.TypeAHeckeAlgebra.regularInnerProductCore

The positive definite regular inner product `⟨x,y⟩ = τ(x* y)`. This core supplies the
normed and inner product space structures without choosing a global norm instance.

```lean
TauCeti.TypeAHeckeAlgebra.regularInnerProductCore.{u_1, u_2} {𝕜 : Type u_1} [RCLike 𝕜] {q : 𝕜ˣ}
  {n : ℕ} [Fact (IsSelfAdjoint ↑q)] {W : Type u_2} [Group W]
  (cs : CoxeterSystem (CoxeterMatrix.A (n - 1)) W) [Finite W] :
  InnerProductSpace.Core 𝕜 (TauCeti.TypeAHeckeAlgebra 𝕜 q n)
```

## Depends on

- [The basis theorem](the-basis-theorem.md)

## Proof depends on

- [The finite presentation is isomorphic to the stage](the-finite-presentation-is-isomorphic-to-the-sta.md)
- [The Hecke algebra on `n` strands embeds in the infinite type-A Hecke algebra, over every commutative ring and for every unit parameter](the-hecke-algebra-on-n-strands-embeds-in-the-inf.md)
- [Matsumoto's theorem, relational form](../../../group-theory/coxeter/matsumotos-theorem-relational-form.md)
- [TauCeti.InfiniteTypeAHeckeAlgebra](tauceti-infinitetypeaheckealgebra.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.TypeAHeckeAlgebra.regularInnerProductCore`](https://taucetiproject.org/docs/TauCeti/Algebra/TypeAHeckeAlgebra/Regular/Form.html#TauCeti.TypeAHeckeAlgebra.regularInnerProductCore).

## Sources

- [Tau Ceti documentation: `TauCeti.TypeAHeckeAlgebra.regularInnerProductCore`](https://taucetiproject.org/docs/TauCeti/Algebra/TypeAHeckeAlgebra/Regular/Form.html#TauCeti.TypeAHeckeAlgebra.regularInnerProductCore)
- [Source of `TauCeti.TypeAHeckeAlgebra.regularInnerProductCore` in TauCeti/Algebra/TypeAHeckeAlgebra/Regular/Form.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/TypeAHeckeAlgebra/Regular/Form.lean#L146)
- [Tau Ceti roadmap status: Type-A Hecke algebras, braid traces, and positive quotients](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/TypeAHeckeAlgebras/STATUS.md)
