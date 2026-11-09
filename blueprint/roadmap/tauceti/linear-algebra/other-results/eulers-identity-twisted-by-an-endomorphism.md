---
declaration: theorem
origin: cited
lean: AlgHom.apply_derivationOfEnd_eq_mul_of_mem_homogeneousSubmodule
statement: formalized
proof: formalized
---

# Euler's identity, twisted by an endomorphism

If an algebra map `φ` turns `f` into
multiplication by `c` on generators, `φ (ι (f x)) = c * φ (ι x)`, then on a homogeneous element of
degree `n` it turns the derivation induced by `f` into multiplication by `n * c`. For `f = 1` and
`φ` the identity this is Euler's identity `D p = n • p` for the Euler derivation `D`.

```lean
AlgHom.apply_derivationOfEnd_eq_mul_of_mem_homogeneousSubmodule.{u, v, u_1} {R : Type u}
  {M : Type v} [CommRing R] [AddCommGroup M] [_root_.Module R M] {A : Type u_1} [CommSemiring A]
  [Algebra R A] (φ : SymmetricAlgebra R M →ₐ[R] A) {f : Module.End R M} {c : A}
  (h : ∀ (x : M), φ ((SymmetricAlgebra.ι R M) (f x)) = c * φ ((SymmetricAlgebra.ι R M) x)) {n : ℕ}
  {p : SymmetricAlgebra R M} (hp : p ∈ TauCeti.SymmetricAlgebra.homogeneousSubmodule R M n) :
  φ (((SymmetricAlgebra.derivationOfEnd R M) f) p) = ↑n * c * φ p
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`AlgHom.apply_derivationOfEnd_eq_mul_of_mem_homogeneousSubmodule`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/SymmetricAlgebra/Derivation/OfEnd.html#AlgHom.apply_derivationOfEnd_eq_mul_of_mem_homogeneousSubmodule).

## Sources

- [Tau Ceti documentation: `AlgHom.apply_derivationOfEnd_eq_mul_of_mem_homogeneousSubmodule`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/SymmetricAlgebra/Derivation/OfEnd.html#AlgHom.apply_derivationOfEnd_eq_mul_of_mem_homogeneousSubmodule)
- [Source of `AlgHom.apply_derivationOfEnd_eq_mul_of_mem_homogeneousSubmodule` in TauCeti/LinearAlgebra/SymmetricAlgebra/Derivation/OfEnd.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/SymmetricAlgebra/Derivation/OfEnd.lean#L111)
