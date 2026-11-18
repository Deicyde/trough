---
catalog: module
lean: Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullBetaEta, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullBetaEta.redex_app_l_cong, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullBetaEta.redex_app_r_cong
statement: formalized
proof: formalized
---

# βη-Confluence for the λ-calculus (FullBetaEta)

`Cslib.Languages.LambdaCalculus.LocallyNameless.Untyped.FullBetaEta`, in [Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullBetaEta.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullBetaEta.lean), by Maximiliano Onofre Martínez, Yijun Leng.

> ## Reference
>
> * [T. Nipkow, *More Church-Rosser Proofs (in Isabelle/HOL)*][Nipkow2001]

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullBetaEta` (abbreviation, [line 36](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullBetaEta.lean#L36))

> Full βη-reduction.

```lean
abbrev FullBetaEta : Term Var → Term Var → Prop
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullBetaEta.redex_app_l_cong` (theorem, [line 40](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullBetaEta.lean#L40))

```lean
theorem redex_app_l_cong (redex : M ↠βηᶠ M') (lc_N : LC N) : app M N ↠βηᶠ app M' N
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullBetaEta.redex_app_r_cong` (theorem, [line 49](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullBetaEta.lean#L49))

```lean
theorem redex_app_r_cong (redex : M ↠βηᶠ M') (lc_N : LC N) : app N M ↠βηᶠ app N M'
```

## Depends on

- [β-reduction for the λ-calculus](fullbeta.md)
- [η-reduction for the λ-calculus](fulleta.md)

## Proof depends on

- [Basic properties of relations](../../../../foundations/relation/basic.md)

## Sources

- [Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullBetaEta.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullBetaEta.lean)
