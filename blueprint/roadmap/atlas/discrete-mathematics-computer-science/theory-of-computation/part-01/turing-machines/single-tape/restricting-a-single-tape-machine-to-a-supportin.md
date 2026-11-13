---
declaration: section
origin: cited
lean: MetaMathlibExt.TM0Restrict.restrict, MetaMathlibExt.TM0Restrict.cfgVal, MetaMathlibExt.TM0Restrict.respects, MetaMathlibExt.TM0Restrict.eval_restrict
statement: formalized
proof: formalized
---

# Restricting a single-tape machine to a supporting set of states

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/restricting-a-single-tape-machine-to-a-supportin/index.html).

## Restriction of a single-tape machine to a supporting set of states

Let $M$ be a single-tape
Turing machine with tape alphabet $\Gamma$ and states $\Lambda$, and let $S \subseteq \Lambda$
support $M$: $S$ contains the default state and every transition of $M$ from a state in $S$ leads to
a state in $S$. The restriction of $M$ to $S$ is the machine with states $S$ that, in state
$q \in S$ reading $a$, does what $M$ does in state $q$ reading $a$: it halts if $M$ halts, and
otherwise performs the same action and moves to the same next state, which lies in $S$.

Formalized by `MetaMathlibExt.TM0Restrict.restrict`, a definition declared in [MathlibExt/Computability/TuringMachine/Translation/TM0Restrict.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Translation/TM0Restrict.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/restricting-a-single-tape-machine-to-a-supportin/index.html#restrict).

## Forgetting the restriction on a configuration

Let $S$ be a set of states of a
single-tape Turing machine with tape alphabet $\Gamma$ and states $\Lambda$. A configuration with
state $q \in S$ and tape $T$ is sent to the configuration with state $q$, viewed as an element of
$\Lambda$, and the same tape $T$.

Formalized by `MetaMathlibExt.TM0Restrict.cfgVal`, a definition declared in [MathlibExt/Computability/TuringMachine/Translation/TM0Restrict.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Translation/TM0Restrict.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/restricting-a-single-tape-machine-to-a-supportin/index.html#cfg-val).

## The original machine simulates the restricted one step for step

Let $S$ be a set of states
supporting a single-tape Turing machine $M$, and relate a configuration of the restriction of $M$
to $S$ to the configuration of $M$ with the same state, viewed as a state of $M$, and the same
tape. Suppose the configuration $c$ of the restricted machine is related to the configuration $d$
of $M$. If the restricted machine steps from $c$ to $c'$, then $M$ reaches, in one or more steps
from $d$, the configuration related to $c'$. If the restricted machine has no step from $c$, then
$M$ has no step from $d$.

Formalized by `MetaMathlibExt.TM0Restrict.respects`, a theorem declared in [MathlibExt/Computability/TuringMachine/Translation/TM0Restrict.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Translation/TM0Restrict.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/restricting-a-single-tape-machine-to-a-supportin/index.html#respects).

## The restricted machine evaluates like the original

Let $M$ be a single-tape Turing machine
with tape alphabet $\Gamma$ and states $\Lambda$, and let $S \subseteq \Lambda$ be a set of states
that supports $M$: it contains the default state and is closed under the transitions of $M$. If the
default state of the restriction of $M$ to $S$ is the default state of $M$, then for every input
list $l$ over $\Gamma$ the evaluation of the restricted machine on $l$ equals that of $M$: either
both fail to halt, or both halt with the same output.

Formalized by `MetaMathlibExt.TM0Restrict.eval_restrict`, a theorem declared in [MathlibExt/Computability/TuringMachine/Translation/TM0Restrict.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/TuringMachine/Translation/TM0Restrict.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/restricting-a-single-tape-machine-to-a-supportin/index.html#eval-restrict).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Restricting a single-tape machine to a supporting set of states](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/restricting-a-single-tape-machine-to-a-supportin/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/turing-machines/single-tape/restricting-a-single-tape-machine-to-a-supportin)
