---
catalog: module
lean: Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Xi, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Xi.step_lc_r, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Xi.step_lc_l
statement: formalized
proof: formalized
---

# Congruence for the λ-calculus

`Cslib.Languages.LambdaCalculus.LocallyNameless.Untyped.Congruence`, in [Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/Congruence.lean](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/Congruence.lean), by Maximiliano Onofre Martínez.

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Xi` (inductive type, [line 24](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/Congruence.lean#L24))

> Congruence closure of a relation.

```lean
inductive Xi (R : Term Var → Term Var → Prop) : Term Var → Term Var → Prop
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Xi.step_lc_r` (lemma, [line 42](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/Congruence.lean#L42))

> The right side of a congruence step is locally closed.

```lean
lemma step_lc_r (hR : ∀ {M' N'}, R M' N' → LC N') (step : Xi R M N) : LC N
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Xi.step_lc_l` (lemma, [line 51](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/Congruence.lean#L51))

> The left side of a congruence step is locally closed.

```lean
lemma step_lc_l (hR : ∀ {M' N'}, R M' N' → LC M') (step : Xi R M N) : LC M
```

## Depends on

- [LcAt](lcat.md)

## Sources

- [Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/Congruence.lean at 8b510d01](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/Congruence.lean)
- [Declaration ledger](../../../../../../sources/cslib/Cslib.Languages.LambdaCalculus.LocallyNameless.Untyped.Congruence.json)
