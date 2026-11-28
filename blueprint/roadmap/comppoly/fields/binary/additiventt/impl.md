---
catalog: module
lean: AdditiveNTT.computableBasisExplicit, AdditiveNTT.computableBasisExplicit_eq_multilinearBasis, AdditiveNTT.hβ_lin_indep_concrete, AdditiveNTT.BTF₃, AdditiveNTT.testNTTBTF₃
statement: formalized
proof: formalized
---

# Concrete additive NTT instances

`CompPoly.Fields.Binary.AdditiveNTT.Impl`, in [CompPoly/Fields/Binary/AdditiveNTT/Impl.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/AdditiveNTT/Impl.lean), by Chung Thai Nguyen, Quang Dao.

> Compatibility entry point for the generic executable additive NTT algorithms, together with
> concrete binary tower bases, instances and the existing example. Generic algorithm clients can
> import `CompPoly.Fields.Binary.AdditiveNTT.Executable`; generic correctness clients can import
> `CompPoly.Fields.Binary.AdditiveNTT.Correctness`.

`AdditiveNTT.computableBasisExplicit` (definition, [line 37](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/AdditiveNTT/Impl.lean#L37))

> Computable basis for ConcreteBTField k over ConcreteBTField 0.
> This is the explicit product of Z's.

```lean
def computableBasisExplicit (k : ℕ) (i : Fin (2 ^ k)) : ConcreteBTField k
```

`AdditiveNTT.computableBasisExplicit_eq_multilinearBasis` (theorem, [line 46](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/AdditiveNTT/Impl.lean#L46))

> The executable bit-indexed basis equals the multilinear tower basis over level zero.

```lean
theorem computableBasisExplicit_eq_multilinearBasis (k : ℕ) :
    computableBasisExplicit k = fun i => multilinearBasis 0 k (by omega) i
```

`AdditiveNTT.hβ_lin_indep_concrete` (theorem, [line 63](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/AdditiveNTT/Impl.lean#L63))

```lean
theorem hβ_lin_indep_concrete (k : ℕ) :
    letI := ConcreteBTFieldAlgebra (l:=0) (r:=k) (h_le:=by omega)
    LinearIndependent (R := ConcreteBTField 0)
      (v := computableBasisExplicit k)
```

`AdditiveNTT.BTF₃` (abbreviation, [line 71](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/AdditiveNTT/Impl.lean#L71))

```lean
abbrev BTF₃
```

`AdditiveNTT.testNTTBTF₃` (definition, [line 87](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/AdditiveNTT/Impl.lean#L87))

> Test of the computable additive NTT over BTF₃ (an 8-bit binary tower field `BTF₃`).
> **Input polynomial:** p(x) = x (novel coefficients [7, 1, 0, 0]) of size `2^ℓ` in `BTF₃`
> - `ℓ = 2`
> - `R_rate = 2`: Repetition rate, evaluating at `S₀` of size `2^(ℓ + R_rate) = 16` points
> - `r = 2^3 = 8`: Dimension of the basis for `BTF₃` over `GF(2)`
> **Output:** A function `Fin 16 → BTF₃` giving the evaluations of `p(x) = x` at 16 points
> in the evaluation domain `S₀` defined by the spanning basis elements `{β₀, ..., β_{ℓ + 𝓡 - 1}}`
> of `BTF₃` over `GF(2)`.

```lean
def testNTTBTF₃ : Fin (2 ^ (2 + 2)) → BTF₃
```

## Depends on

- [Executable additive NTT algorithms](executable.md)
- [Concrete Binary Tower Basis](../tower/concrete/basis.md)

## Sources

- [CompPoly/Fields/Binary/AdditiveNTT/Impl.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/AdditiveNTT/Impl.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Fields.Binary.AdditiveNTT.Impl.json)
