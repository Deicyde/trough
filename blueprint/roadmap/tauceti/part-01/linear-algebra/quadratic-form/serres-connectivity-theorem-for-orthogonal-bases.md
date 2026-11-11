---
declaration: theorem
origin: cited
lean: Module.Basis.reflTransGen_isOrtho_isContiguous
statement: formalized
proof: formalized
---

# Serre's connectivity theorem for orthogonal bases

Orthogonal bases of a regular
quadratic space in dimension at least three are joined by a finite chain whose every step
consists of two orthogonal bases with a vector in common.

```lean
Module.Basis.reflTransGen_isOrtho_isContiguous.{u_1, u_2} {K : Type u_1} {V : Type u_2} [Field K]
  [Invertible 2] [AddCommGroup V] [_root_.Module K V] {Q : QuadraticForm K V} {n : ℕ}
  (b b' : Module.Basis (Fin (n + 3)) K V) (hQ : QuadraticMap.Nondegenerate)
  (hb : LinearMap.IsOrthoᵢ (QuadraticMap.associated Q) ⇑b)
  (hb' : LinearMap.IsOrthoᵢ (QuadraticMap.associated Q) ⇑b') :
  Relation.ReflTransGen
    (fun c c' =>
      LinearMap.IsOrthoᵢ (QuadraticMap.associated Q) ⇑c ∧
        LinearMap.IsOrthoᵢ (QuadraticMap.associated Q) ⇑c' ∧ c.IsContiguous c')
    b b'
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Module.Basis.reflTransGen_isOrtho_isContiguous`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/QuadraticForm/Diagonal/Contiguous/Connected.html#Module.Basis.reflTransGen_isOrtho_isContiguous).

## Sources

- [Tau Ceti documentation: `Module.Basis.reflTransGen_isOrtho_isContiguous`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/QuadraticForm/Diagonal/Contiguous/Connected.html#Module.Basis.reflTransGen_isOrtho_isContiguous)
- [Source of `Module.Basis.reflTransGen_isOrtho_isContiguous` in TauCeti/LinearAlgebra/QuadraticForm/Diagonal/Contiguous/Connected.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/QuadraticForm/Diagonal/Contiguous/Connected.lean#L67)
