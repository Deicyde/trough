---
declaration: theorem
origin: cited
lean: TauCeti.TemperleyLieb.span_strandIncl_union_strandIncl_mul_e_last_mul_eq_top
statement: formalized
proof: formalized
---

# The tower normal form

The Temperley–Lieb algebra on `n + 2` strands is spanned by the
image `strandIncl a` of the algebra on `n + 1` strands, together with the products
`strandIncl a * e δ (Fin.last n) * strandIncl b`: as `R`-modules,
`TL(n + 2) = TL(n + 1) + TL(n + 1) · e (Fin.last n) · TL(n + 1)`.

```lean
TauCeti.TemperleyLieb.span_strandIncl_union_strandIncl_mul_e_last_mul_eq_top.{u_1} {R : Type u_1}
  [CommSemiring R] {δ : R} (n : ℕ) :
  Submodule.span R
      (Set.range ⇑TauCeti.TemperleyLieb.strandIncl ∪
        Set.range fun p =>
          TauCeti.TemperleyLieb.strandIncl p.1 * TauCeti.TemperleyLieb.e δ (Fin.last n) *
            TauCeti.TemperleyLieb.strandIncl p.2) =
    ⊤
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.TemperleyLieb.span_strandIncl_union_strandIncl_mul_e_last_mul_eq_top`](https://taucetiproject.org/docs/TauCeti/Algebra/TemperleyLieb/Tower.html#TauCeti.TemperleyLieb.span_strandIncl_union_strandIncl_mul_e_last_mul_eq_top).

## Sources

- [Tau Ceti documentation: `TauCeti.TemperleyLieb.span_strandIncl_union_strandIncl_mul_e_last_mul_eq_top`](https://taucetiproject.org/docs/TauCeti/Algebra/TemperleyLieb/Tower.html#TauCeti.TemperleyLieb.span_strandIncl_union_strandIncl_mul_e_last_mul_eq_top)
- [Source of `TauCeti.TemperleyLieb.span_strandIncl_union_strandIncl_mul_e_last_mul_eq_top` in TauCeti/Algebra/TemperleyLieb/Tower.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/TemperleyLieb/Tower.lean#L169)
- [Tau Ceti roadmap status: Temperley–Lieb diagrams, categories, and algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/TemperleyLieb/STATUS.md)
