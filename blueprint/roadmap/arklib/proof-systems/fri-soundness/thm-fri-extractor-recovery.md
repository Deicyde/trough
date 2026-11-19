---
declaration: theorem
origin: cited
lean: Fri.Spec.Extractor.extractHistory_eq_some_of_safeHistory, Fri.Spec.Extractor.extractHistory_eq_some_of_density
statement: formalized
proof: formalized
---

# fri-extractor-recovery

Fix a safe retained history at threshold $\theta$, whose final polynomial has degree less than $d$. Let $A$ be its accepting initial-domain positions. If $N(1-\theta)\leq |A|$ and $M\leq |A|$, the named extractor returns a polynomial of degree less than $M$ agreeing with the initial word on all of $A$. Consequently, if $\tau\leq\theta$, $\tau\leq 1-M/N$, and $N(1-\tau)\leq |A|$, the returned witness has relative distance at most $\tau$.

## Depends on

- [fri-measured-extractor](def-fri-measured-extractor.md)
- [fri-coefficient-lift](lem-fri-coefficient-lift.md)

## Proof

Safe-history agreement lifting supplies one degree-bounded codeword agreeing on $A$. The first $M$ cached nodes are distinct accepting positions, so polynomial uniqueness identifies their measured interpolant with that codeword. The final degree guard therefore succeeds. Disagreements are confined to the complement of $A$, giving relative distance at most $1-|A|/N$.

## Lean

Formalized as [`Fri.Spec.Extractor.extractHistory_eq_some_of_safeHistory`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Fri.Spec.Extractor.extractHistory_eq_some_of_safeHistory), [`Fri.Spec.Extractor.extractHistory_eq_some_of_density`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Fri.Spec.Extractor.extractHistory_eq_some_of_density).

## Sources

- [ArkLib blueprint: proof_systems/fri.tex, line 155](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/fri.tex#L155)
