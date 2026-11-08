---
declaration: def
origin: cited
lean: Module.IsPseudoNull
statement: formalized
---

# Pseudo-nullity and short exact sequences

Over any commutative ring,
[`Module.IsPseudoNull`](https://github.com/FormalFrontier/iwasawa-modules/blob/e71db96b779b35bb05bd64eec63393e57b8da691/IwasawaModules/PseudoIsomorphism/Basic.lean#L30)
says a module's support avoids primes of height at most one; equivalently,
[each such localization vanishes](https://github.com/FormalFrontier/iwasawa-modules/blob/e71db96b779b35bb05bd64eec63393e57b8da691/IwasawaModules/PseudoIsomorphism/Basic.lean#L34).
Submodules, quotients and extensions preserve pseudo-nullity, and in a short
exact sequence the middle term is pseudo-null exactly when both endpoints
are ([exact-sequence criterion](https://github.com/FormalFrontier/iwasawa-modules/blob/e71db96b779b35bb05bd64eec63393e57b8da691/IwasawaModules/PseudoIsomorphism/Basic.lean#L75)).
The predicate needs no finite-generation, Noetherianity or domain hypothesis.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/iwasawa-modules/blob/e71db96b779b35bb05bd64eec63393e57b8da691/README.md#headline-results) of [FormalFrontier/iwasawa-modules](https://github.com/FormalFrontier/iwasawa-modules) at commit [e71db96b](https://github.com/FormalFrontier/iwasawa-modules/tree/e71db96b779b35bb05bd64eec63393e57b8da691), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Module.IsPseudoNull` (def), declared in [IwasawaModules/PseudoIsomorphism/Basic.lean, line 30](https://github.com/FormalFrontier/iwasawa-modules/blob/e71db96b779b35bb05bd64eec63393e57b8da691/IwasawaModules/PseudoIsomorphism/Basic.lean#L30).

Read from the source at commit [e71db96b](https://github.com/FormalFrontier/iwasawa-modules/tree/e71db96b779b35bb05bd64eec63393e57b8da691), without running Lean.

## Sources

- [iwasawa-modules at e71db96b: README, headline results](https://github.com/FormalFrontier/iwasawa-modules/blob/e71db96b779b35bb05bd64eec63393e57b8da691/README.md#headline-results)
- [Source of `Module.IsPseudoNull` in IwasawaModules/PseudoIsomorphism/Basic.lean](https://github.com/FormalFrontier/iwasawa-modules/blob/e71db96b779b35bb05bd64eec63393e57b8da691/IwasawaModules/PseudoIsomorphism/Basic.lean#L30)
