---
declaration: section
origin: cited
lean: Cslib.Languages.LambdaCalculus.FOmega.fundamental, Cslib.Languages.LambdaCalculus.FOmega.fundamental_closed, Cslib.Languages.LambdaCalculus.FOmega.higherIdType, Cslib.Languages.LambdaCalculus.FOmega.higherId, Cslib.Languages.LambdaCalculus.FOmega.higherId_typed, Cslib.Languages.LambdaCalculus.FOmega.higher_kinded_identity, Cslib.Languages.LambdaCalculus.FOmega.higher_kinded_related, Cslib.Languages.LambdaCalculus.FOmega.forall_var_uninhabited
statement: formalized
proof: formalized
---

# Higher-kinded relational parametricity of pure Fω

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/higher-kinded-relational-parametricity-of-pure-f/index.html).

## Fundamental theorem of higher-kinded parametricity for Fω

The full binary higher-kinded fundamental theorem of pure Fω.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.fundamental`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Parametricity.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/Parametricity.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/higher-kinded-relational-parametricity-of-pure-f/index.html#fundamental).

## Closed typed Fω terms are related to themselves

Every closed-term typed expression is related to itself at every kind environment.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.fundamental_closed`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Parametricity.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/Parametricity.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/higher-kinded-relational-parametricity-of-pure-f/index.html#fundamental-closed).

## Higher-kinded identity type

A genuine higher-kind identity type: `∀ F : * → *, ∀ X : *, F X → F X`.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.higherIdType`, a definition declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Parametricity.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/Parametricity.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/higher-kinded-relational-parametricity-of-pure-f/index.html#higher-id-type).

## Higher-kinded polymorphic identity term

The pure higher-kinded polymorphic identity term.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.higherId`, a definition declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Parametricity.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/Parametricity.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/higher-kinded-relational-parametricity-of-pure-f/index.html#higher-id).

## Typing of the higher-kinded identity

The higher-kinded identity is typed in every existing term context.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.higherId_typed`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Parametricity.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/Parametricity.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/higher-kinded-relational-parametricity-of-pure-f/index.html#higher-id-typed).

## Closed inhabitants of the higher-kinded identity type are identities

Every closed-term inhabitant is beta-identity at every kind-correct instantiation.

The inhabitant is arbitrary, not the manually defined `higherId`. The input
is any locally closed model term; no CBV termination or normalization is claimed.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.higher_kinded_identity`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Parametricity.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/Parametricity.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/higher-kinded-relational-parametricity-of-pure-f/index.html#higher-kinded-identity).

## Higher-kinded identity inhabitants preserve admissible relations

Different higher-kind type instantiations preserve every admissible binary relation.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.higher_kinded_related`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Parametricity.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/Parametricity.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/higher-kinded-relational-parametricity-of-pure-f/index.html#higher-kinded-related).

## No closed Fω term inhabits $\forall X, X$

The empty relation excludes all closed-term inhabitants of `∀ X : *, X`.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.forall_var_uninhabited`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Parametricity.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/Parametricity.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/higher-kinded-relational-parametricity-of-pure-f/index.html#forall-var-uninhabited).

## No closed Fω term inhabits $\forall F, \forall X, F\,X$

A constant empty operator excludes `∀ F : * → *, ∀ X : *, F X`.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.higher_result_uninhabited`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Parametricity.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/Parametricity.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/higher-kinded-relational-parametricity-of-pure-f/index.html#higher-result-uninhabited).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Higher-kinded relational parametricity of pure Fω](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/higher-kinded-relational-parametricity-of-pure-f/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/higher-kinded-relational-parametricity-of-pure-f)
