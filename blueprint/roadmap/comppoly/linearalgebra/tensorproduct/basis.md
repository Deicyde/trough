---
catalog: module
lean: Module.Basis.baseChangeRight, Module.Basis.baseChangeRight_repr_tmul, Module.Basis.baseChangeRight_apply
statement: formalized
proof: formalized
---

# Bases for the right scalar action on tensor products

`CompPoly.LinearAlgebra.TensorProduct.Basis`, in [CompPoly/LinearAlgebra/TensorProduct/Basis.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/TensorProduct/Basis.lean), by Chung Thai Nguyen, Quang Dao.

> `Module.Basis.baseChangeRight` lifts a basis of `Left` over `K` to a basis of
> `Left ⊗[K] Right` over `Right`, with scalars acting on the right tensor factor.
> The action is explicit in each declaration; importing this module preserves Mathlib's
> default action on the left factor, including when `Left = Right`.
>
> For equal factors, select the right `Algebra`, `Module`, `DistribMulAction` and `SMul`
> locally when combining this basis with scalar notation and module laws. Tensor products
> provide independent default instances at each of these levels.
>
> For background on tensor-product bases, see [Lan02]. For equal field factors, this
> right-action basis is the basis used for the row representation in [DP24], §2.5.
>
> ## References
>
> * [Lang, S., *Algebra*][Lan02]
> * [Diamond, B. E. and Posen, J., *Polylogarithmic proofs for multilinears over binary towers*][DP24]

`Module.Basis.baseChangeRight` (definition, [line 43](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/TensorProduct/Basis.lean#L43))

> Lift a `K`-basis of `Left` to a `Right`-basis of `Left ⊗[K] Right`, using the
> right-factor scalar action. This is the right-sided counterpart to `Basis.baseChange`.

```lean
noncomputable def baseChangeRight (b : Basis ι K Left) :
    letI rightAlgebra := Algebra.TensorProduct.rightAlgebra (R := K) (A := Left) (B := Right)
    letI := rightAlgebra.toModule
    Basis ι Right (Left ⊗[K] Right)
```

`Module.Basis.baseChangeRight_repr_tmul` (lemma, [line 53](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/TensorProduct/Basis.lean#L53))

> Coordinates of a pure tensor in the basis for the right-factor scalar action.

```lean
lemma baseChangeRight_repr_tmul (b : Basis ι K Left) (x : Left) (y : Right) (i : ι) :
    letI rightAlgebra := Algebra.TensorProduct.rightAlgebra (R := K) (A := Left) (B := Right)
    letI := rightAlgebra.toModule
    (b.baseChangeRight (Right := Right)).repr (x ⊗ₜ[K] y) i = b.repr x i • y
```

`Module.Basis.baseChangeRight_apply` (lemma, [line 65](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/TensorProduct/Basis.lean#L65))

> The right-action basis vectors are the original basis vectors tensored with one.

```lean
lemma baseChangeRight_apply (b : Basis ι K Left) (i : ι) :
    letI rightAlgebra := Algebra.TensorProduct.rightAlgebra (R := K) (A := Left) (B := Right)
    letI := rightAlgebra.toModule
    b.baseChangeRight (Right := Right) i = b i ⊗ₜ[K] 1
```

## Depends on

Its statements use no other CompPoly module's declarations.

## Sources

- [CompPoly/LinearAlgebra/TensorProduct/Basis.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/TensorProduct/Basis.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.LinearAlgebra.TensorProduct.Basis.json)
