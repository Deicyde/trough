---
catalog: module
lean: CPoly.mem_vars_iff_degreeOf_pos, CPoly.degrees_equiv, CPoly.vars_equiv, CPoly.degreeOf_zero, CPoly.degrees_zero, CPoly.vars_zero, CPoly.degrees_one, CPoly.vars_add_subset
statement: formalized
proof: formalized
---

# Lemmas for `CMvPolynomial.vars` and `CMvPolynomial.degrees`

`CompPoly.Multivariate.VarsDegrees`, in [CompPoly/Multivariate/VarsDegrees.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multivariate/VarsDegrees.lean), by Fawad Haider.

> Correctness lemmas relating `vars`, `degrees`, and `degreeOf` to Mathlib's `MvPolynomial`.
>
> …

`CPoly.mem_vars_iff_degreeOf_pos` (lemma, [line 29](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multivariate/VarsDegrees.lean#L29))

> `i ∈ p.vars` iff `0 < p.degreeOf i`.

```lean
lemma mem_vars_iff_degreeOf_pos [Zero R]
    (i : Fin n) (p : CMvPolynomial n R) :
    i ∈ p.vars ↔ 0 < p.degreeOf i
```

`CPoly.degrees_equiv` (lemma, [line 35](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multivariate/VarsDegrees.lean#L35))

> `degrees` agrees with `MvPolynomial.degrees` via `fromCMvPolynomial`.

```lean
lemma degrees_equiv [CommSemiring R] [BEq R] [LawfulBEq R]
    (p : CMvPolynomial n R) :
    p.degrees = (fromCMvPolynomial p).degrees
```

`CPoly.vars_equiv` (lemma, [line 44](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multivariate/VarsDegrees.lean#L44))

> `vars` agrees with `MvPolynomial.vars` via `fromCMvPolynomial`.

```lean
lemma vars_equiv [CommSemiring R] [BEq R] [LawfulBEq R]
    (p : CMvPolynomial n R) :
    p.vars = (fromCMvPolynomial p).vars
```

`CPoly.degreeOf_zero` (lemma, [line 57](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multivariate/VarsDegrees.lean#L57))

> `(0 : CMvPolynomial n R).degreeOf i = 0`.

```lean
lemma degreeOf_zero [Zero R] [BEq R] [LawfulBEq R]
    (i : Fin n) :
    (0 : CMvPolynomial n R).degreeOf i = 0
```

`CPoly.degrees_zero` (lemma, [line 68](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multivariate/VarsDegrees.lean#L68))

> `(0 : CMvPolynomial n R).degrees = 0`.

```lean
lemma degrees_zero [Zero R] [BEq R] [LawfulBEq R] :
    (0 : CMvPolynomial n R).degrees = 0
```

`CPoly.vars_zero` (lemma, [line 74](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multivariate/VarsDegrees.lean#L74))

> `(0 : CMvPolynomial n R).vars = ∅`.

```lean
lemma vars_zero [Zero R] [BEq R] [LawfulBEq R] :
    (0 : CMvPolynomial n R).vars = ∅
```

`CPoly.degrees_one` (lemma, [line 80](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multivariate/VarsDegrees.lean#L80))

> `(1 : CMvPolynomial n R).degrees = 0`.

```lean
lemma degrees_one [CommSemiring R] [BEq R] [LawfulBEq R] :
    (1 : CMvPolynomial n R).degrees = 0
```

`CPoly.vars_add_subset` (lemma, [line 85](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multivariate/VarsDegrees.lean#L85))

> `(p + q).vars ⊆ p.vars ∪ q.vars`.

```lean
lemma vars_add_subset [CommSemiring R] [BEq R] [LawfulBEq R]
    (p q : CMvPolynomial n R) :
    (p + q).vars ⊆ p.vars ∪ q.vars
```

## Depends on

- [`CMvPolynomial`/`MvPolynomial` Core](mvpolyequiv/core.md)

## Proof depends on

- [`CMvPolynomial`/`MvPolynomial` Evaluation](mvpolyequiv/eval.md)

## Sources

- [CompPoly/Multivariate/VarsDegrees.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multivariate/VarsDegrees.lean)
- [Declaration ledger](../../../sources/comppoly/CompPoly.Multivariate.VarsDegrees.json)
