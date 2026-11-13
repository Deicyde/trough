---
declaration: section
origin: cited
lean: Cslib.Decidability.descLength, Cslib.Decidability.MinimalCode, Cslib.Decidability.exists_code_dom_singleton, Cslib.Decidability.exists_minimalCode_dom, Cslib.Decidability.exists_minimalCode_gt, Cslib.Decidability.not_tm2Recognizable_minimalCode
statement: formalized
proof: formalized
---

# Minimal programs

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/minimal-programs/index.html).

## Description length of a code

For a code $c$ of a partial recursive function, the
description length of $c$ is the number of binary digits of the encoding of $c$ as a natural
number, that is, the least $k$ such that this encoding is less than $2^k$ (so it is $0$ when the
encoding is $0$).

Formalized by `Cslib.Decidability.descLength`, a definition declared in [CSLibExt/Computability/Decidability/Minimal.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Minimal.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/minimal-programs/index.html#desc-length).

## Minimal codes

A code $c$ of a partial recursive function is minimal when no code with a
shorter description has the same domain: for every code $d$ whose description length is strictly
less than that of $c$, the domain of $d$ (the set of inputs on which its evaluation is defined)
differs from the domain of $c$. The set of minimal codes is denoted $\mathrm{MIN}$.

Formalized by `Cslib.Decidability.MinimalCode`, a definition declared in [CSLibExt/Computability/Decidability/Minimal.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Minimal.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/minimal-programs/index.html#minimal-code).

## Codes with singleton domain

For every natural number $n$ there is a code $c$ of a partial
recursive function whose evaluation is defined exactly at $n$, that is, the domain of the partial
function computed by $c$ is $\{n\}$.

Formalized by `Cslib.Decidability.exists_code_dom_singleton`, a theorem declared in [CSLibExt/Computability/Decidability/Minimal.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Minimal.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/minimal-programs/index.html#exists-code-dom-singleton).

## Every language of a code has a minimal code

For every code $c$ of a partial recursive
function there is a minimal code $D$ whose domain equals the domain of $c$, where the domain of a
code is the set of inputs on which its evaluation is defined.

Formalized by `Cslib.Decidability.exists_minimalCode_dom`, a theorem declared in [CSLibExt/Computability/Decidability/Minimal.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Minimal.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/minimal-programs/index.html#exists-minimal-code-dom).

## Minimal codes are unbounded

For every natural number $N$ there is a minimal code $D$ of a
partial recursive function whose encoding as a natural number is greater than $N$.

Formalized by `Cslib.Decidability.exists_minimalCode_gt`, a theorem declared in [CSLibExt/Computability/Decidability/Minimal.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Minimal.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/minimal-programs/index.html#exists-minimal-code-gt).

## Minimal codes are not recognizable

The set $\mathrm{MIN}$ of minimal codes of partial
recursive functions is not recognizable by a multi-stack Turing machine: there is no finite
multi-stack machine that, for every code $c$, halts on the binary encoding of the natural-number
encoding of $c$ exactly when $c$ is minimal.

## Sources

- M. Sipser, Introduction to the Theory of Computation, 3rd ed., Theorem 6.7.

Formalized by `Cslib.Decidability.not_tm2Recognizable_minimalCode`, a theorem declared in [CSLibExt/Computability/Decidability/Minimal.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Minimal.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/minimal-programs/index.html#not-tm2-recognizable-minimal-code).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Minimal programs](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/minimal-programs/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/computability/minimal-programs)
