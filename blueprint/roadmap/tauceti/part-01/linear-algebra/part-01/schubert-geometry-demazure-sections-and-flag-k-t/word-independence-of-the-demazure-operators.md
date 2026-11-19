---
declaration: theorem
origin: cited
lean: RootPairing.prod_map_demazureOperator_eq_of_wordProd_eq
statement: formalized
proof: formalized
---

# Word independence of the Demazure operators

the product `D_{k₁} ⋯ D_{kᵣ}` of the Demazure
operators along a reduced word in the simple reflections of a base depends only on the element
`s_{k₁} ⋯ s_{kᵣ}` of the Weyl group that the word spells.

```lean
RootPairing.prod_map_demazureOperator_eq_of_wordProd_eq.{u_1, u_2, u_3} {ι : Type u_1}
  {M : Type u_2} {N : Type u_3} [AddCommGroup M] [AddCommGroup N] (P : RootPairing ι ℤ M N)
  [Finite ι] (b : P.Base) [P.IsReduced] {ω ω' : List ↥b.support}
  (hω : (TauCeti.weylCoxeterSystem P b).IsReduced ω)
  (hω' : (TauCeti.weylCoxeterSystem P b).IsReduced ω')
  (h : (TauCeti.weylCoxeterSystem P b).wordProd ω = (TauCeti.weylCoxeterSystem P b).wordProd ω') :
  (List.map (fun m => P.demazureOperator ↑m) ω).prod =
    (List.map (fun m => P.demazureOperator ↑m) ω').prod
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Matsumoto's theorem, relational form](../../../group-theory/coxeter/matsumotos-theorem-relational-form.md)

## Lean

Formalized in Tau Ceti as [`RootPairing.prod_map_demazureOperator_eq_of_wordProd_eq`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/RootSystem/Weyl/Demazure/Braid.html#RootPairing.prod_map_demazureOperator_eq_of_wordProd_eq).

## Sources

- [Tau Ceti documentation: `RootPairing.prod_map_demazureOperator_eq_of_wordProd_eq`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/RootSystem/Weyl/Demazure/Braid.html#RootPairing.prod_map_demazureOperator_eq_of_wordProd_eq)
- [Source of `RootPairing.prod_map_demazureOperator_eq_of_wordProd_eq` in TauCeti/LinearAlgebra/RootSystem/Weyl/Demazure/Braid.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/LinearAlgebra/RootSystem/Weyl/Demazure/Braid.lean#L736)
- [Tau Ceti roadmap status: Schubert geometry, Demazure sections and flag K-theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SchubertGeometry/STATUS.md)
