---
catalog: module
lean: definingPoly, degree_s_smul_X, degree_s_smul_X_add_1, definingPoly_is_monic, degree_definingPoly, natDegree_definingPoly, definingPoly_ne_zero, definingPoly_is_not_unit, definingPoly_coeffOf0, definingPoly_coeffOf1
statement: formalized
proof: formalized
---

# Binary Tower Defining Polynomials

`CompPoly.Fields.Binary.Tower.Support.DefiningPoly`, in [CompPoly/Fields/Binary/Tower/Support/DefiningPoly.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Support/DefiningPoly.lean), by Quang Dao, Chung Thai Nguyen.

> Defining polynomials and basic degree lemmas used by the binary tower files.

`definingPoly` (definition, [line 24](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Support/DefiningPoly.lean#L24))

```lean
noncomputable def definingPoly {F : Type*} [instField : Field F] (s : F)
```

`degree_s_smul_X` (lemma, [line 27](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Support/DefiningPoly.lean#L27))

```lean
lemma degree_s_smul_X {F : Type*} [Field F] [Fintype F] (s : F) [NeZero s] :
    (C s * (X : (F)[X])).degree = 1
```

`degree_s_smul_X_add_1` (lemma, [line 32](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Support/DefiningPoly.lean#L32))

```lean
lemma degree_s_smul_X_add_1 {F : Type*} [Field F] [Fintype F] (s : F) [NeZero s] :
    (C s * (X : (F)[X]) + 1).degree = 1
```

`definingPoly_is_monic` (lemma, [line 38](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Support/DefiningPoly.lean#L38))

```lean
lemma definingPoly_is_monic {F : Type*} [Field F] [Fintype F] (s : F) [NeZero s] :
    (definingPoly s).Monic
```

`degree_definingPoly` (lemma, [line 55](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Support/DefiningPoly.lean#L55))

```lean
lemma degree_definingPoly {F : Type*} [Field F] [Fintype F] (s : F) [NeZero s] :
    (definingPoly s).degree = 2
```

`natDegree_definingPoly` (lemma, [line 66](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Support/DefiningPoly.lean#L66))

```lean
lemma natDegree_definingPoly {F : Type*} [Field F] [Fintype F] (s : F) [NeZero s] :
    (definingPoly s).natDegree = 2
```

`definingPoly_ne_zero` (lemma, [line 69](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Support/DefiningPoly.lean#L69))

```lean
lemma definingPoly_ne_zero {F : Type*} [Field F] [Fintype F] (s : F) [NeZero s] :
    (definingPoly s) ≠ 0
```

`definingPoly_is_not_unit` (lemma, [line 75](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Support/DefiningPoly.lean#L75))

```lean
lemma definingPoly_is_not_unit {F : Type*} [Field F] [Fintype F] (s : F) [NeZero s] :
    ¬IsUnit (definingPoly s)
```

`definingPoly_coeffOf0` (lemma, [line 87](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Support/DefiningPoly.lean#L87))

```lean
lemma definingPoly_coeffOf0 {F : Type*} [Field F] [Fintype F] (s : F) [NeZero s] :
    (definingPoly s).coeff 0 = 1
```

`definingPoly_coeffOf1` (lemma, [line 93](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Support/DefiningPoly.lean#L93))

```lean
lemma definingPoly_coeffOf1 {F : Type*} [Field F] [Fintype F] (s : F) [NeZero s] :
    (definingPoly s).coeff 1 = s
```

## Depends on

Its statements use no other CompPoly module's declarations.

## Proof depends on

- [Binary Tower Preliminaries](preliminaries.md)

## Sources

- [CompPoly/Fields/Binary/Tower/Support/DefiningPoly.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Support/DefiningPoly.lean)
- [Declaration ledger](../../../../../../sources/comppoly/CompPoly.Fields.Binary.Tower.Support.DefiningPoly.json)
