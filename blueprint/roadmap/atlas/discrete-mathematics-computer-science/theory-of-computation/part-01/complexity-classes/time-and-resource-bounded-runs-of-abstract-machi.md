---
declaration: section
origin: cited
lean: Cslib.OutputReachability.next, Cslib.OutputReachability.boundedStep, Cslib.OutputReachability.ReachesOutput, Cslib.OutputReachability.Runs, Cslib.OutputReachability.iterate_of_some, Cslib.OutputReachability.ReachesOutput.halt, Cslib.OutputReachability.ReachesOutput.prepend, Cslib.OutputReachability.relatesInSteps_iterate
statement: formalized
proof: formalized
---

# Time- and resource-bounded runs of abstract machines

20 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-resource-bounded-runs-of-abstract-machi/index.html).

## One iteration step with absorbing halted states

One iteration, preserving a state once its output is available.

Formalized by `Cslib.OutputReachability.next`, a definition declared in [CSLibExt/Foundations/Relation/OutputReachability.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Foundations/Relation/OutputReachability.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-resource-bounded-runs-of-abstract-machi/index.html#next).

## Resource-bounded active step

An active step with a resource bound on its source.

Formalized by `Cslib.OutputReachability.boundedStep`, a definition declared in [CSLibExt/Foundations/Relation/OutputReachability.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Foundations/Relation/OutputReachability.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-resource-bounded-runs-of-abstract-machi/index.html#bounded-step).

## Output reachability within time and resource bounds

Reach an output in at most `T` active steps, with every state bounded by `S`.

Formalized by `Cslib.OutputReachability.ReachesOutput`, a definition declared in [CSLibExt/Foundations/Relation/OutputReachability.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Foundations/Relation/OutputReachability.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-resource-bounded-runs-of-abstract-machi/index.html#reaches-output).

## Bounded run from an input's initial state

Reach an output starting from an input's initial state.

Formalized by `Cslib.OutputReachability.Runs`, a definition declared in [CSLibExt/Foundations/Relation/OutputReachability.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Foundations/Relation/OutputReachability.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-resource-bounded-runs-of-abstract-machi/index.html#runs).

## Iterates of a halted state are constant

Every iterate of an already halted state is that state.

Formalized by `Cslib.OutputReachability.iterate_of_some`, a theorem declared in [CSLibExt/Foundations/Relation/OutputReachability.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Foundations/Relation/OutputReachability.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-resource-bounded-runs-of-abstract-machi/index.html#iterate-of-some).

## A halted state reaches its output with any time budget

A halted state reaches its output with any remaining time budget.

Formalized by `Cslib.OutputReachability.ReachesOutput.halt`, a theorem declared in [CSLibExt/Foundations/Relation/OutputReachability.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Foundations/Relation/OutputReachability.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-resource-bounded-runs-of-abstract-machi/index.html#halt).

## Prepending a bounded step to a successful computation

Prepend an active bounded step to a successful computation.

Formalized by `Cslib.OutputReachability.ReachesOutput.prepend`, a theorem declared in [CSLibExt/Foundations/Relation/OutputReachability.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Foundations/Relation/OutputReachability.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-resource-bounded-runs-of-abstract-machi/index.html#prepend).

## Canonical finite path to an output bounds all iterates

A canonical finite path ending in an output has the source's all-iterate bounds.

Formalized by `Cslib.OutputReachability.relatesInSteps_iterate`, a theorem declared in [CSLibExt/Foundations/Relation/OutputReachability.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Foundations/Relation/OutputReachability.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-resource-bounded-runs-of-abstract-machi/index.html#relates-in-steps-iterate).

## Output reachability gives stable outputs and bounded iterates

Reachability gives stable outputs after the budget and bounds every iterate.

Formalized by `Cslib.OutputReachability.ReachesOutput.iterate`, a theorem declared in [CSLibExt/Foundations/Relation/OutputReachability.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Foundations/Relation/OutputReachability.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-resource-bounded-runs-of-abstract-machi/index.html#iterate).

## Output reachability from the iteration condition

The source iteration condition constructs a canonical bounded path.

Formalized by `Cslib.OutputReachability.reachesOutput_of_iterate`, a theorem declared in [CSLibExt/Foundations/Relation/OutputReachability.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Foundations/Relation/OutputReachability.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-resource-bounded-runs-of-abstract-machi/index.html#reaches-output-of-iterate).

## Characterization of output reachability by iterates

Exact source characterization, including bounds on all natural-number iterates.

Formalized by `Cslib.OutputReachability.reachesOutput_iff_iterate`, a theorem declared in [CSLibExt/Foundations/Relation/OutputReachability.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Foundations/Relation/OutputReachability.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-resource-bounded-runs-of-abstract-machi/index.html#reaches-output-iff-iterate).

## Terminal iterates are stable

A terminal iterate remains unchanged at every later iteration count.

Formalized by `Cslib.OutputReachability.iterate_stable`, a theorem declared in [CSLibExt/Foundations/Relation/OutputReachability.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Foundations/Relation/OutputReachability.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-resource-bounded-runs-of-abstract-machi/index.html#iterate-stable).

## Output reachability via bounded iterates after halting

Finite visited-state bounds are equivalent to all-iterate bounds after halting.

Formalized by `Cslib.OutputReachability.reachesOutput_iff_bounded_iterate`, a theorem declared in [CSLibExt/Foundations/Relation/OutputReachability.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Foundations/Relation/OutputReachability.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-resource-bounded-runs-of-abstract-machi/index.html#reaches-output-iff-bounded-iterate).

## Monotonicity of output reachability in the bounds

Increasing either bound preserves reachability.

Formalized by `Cslib.OutputReachability.ReachesOutput.mono`, a theorem declared in [CSLibExt/Foundations/Relation/OutputReachability.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Foundations/Relation/OutputReachability.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-resource-bounded-runs-of-abstract-machi/index.html#mono).

## Uniqueness of reached outputs

Output values reached from the same state are unique, regardless of bounds.

Formalized by `Cslib.OutputReachability.ReachesOutput.unique`, a theorem declared in [CSLibExt/Foundations/Relation/OutputReachability.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Foundations/Relation/OutputReachability.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-resource-bounded-runs-of-abstract-machi/index.html#unique).

## Input-initialized iteration with absorbing halting

Iteration initialized by an input, with absorbing halting.

Formalized by `Cslib.OutputReachability.run`, a definition declared in [CSLibExt/Foundations/Relation/OutputReachability.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Foundations/Relation/OutputReachability.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-resource-bounded-runs-of-abstract-machi/index.html#run).

## Characterization of bounded runs by initialized iteration

The source `Runs` interface, stated using initialized iteration.

Formalized by `Cslib.OutputReachability.runs_iff_iterate`, a theorem declared in [CSLibExt/Foundations/Relation/OutputReachability.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Foundations/Relation/OutputReachability.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-resource-bounded-runs-of-abstract-machi/index.html#runs-iff-iterate).

## The output of a successful run persists

The output of a successful initialized run is present at every later time.

Formalized by `Cslib.OutputReachability.Runs.out_run`, a theorem declared in [CSLibExt/Foundations/Relation/OutputReachability.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Foundations/Relation/OutputReachability.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-resource-bounded-runs-of-abstract-machi/index.html#out-run).

## Monotonicity of bounded runs in time and resources

Increasing time and resource bounds preserves initialized runs.

Formalized by `Cslib.OutputReachability.Runs.mono`, a theorem declared in [CSLibExt/Foundations/Relation/OutputReachability.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Foundations/Relation/OutputReachability.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-resource-bounded-runs-of-abstract-machi/index.html#mono-2).

## Uniqueness of run outputs

Initialized runs have unique outputs.

Formalized by `Cslib.OutputReachability.Runs.unique`, a theorem declared in [CSLibExt/Foundations/Relation/OutputReachability.lean, line 204](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Foundations/Relation/OutputReachability.lean#L204). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-resource-bounded-runs-of-abstract-machi/index.html#unique-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Time- and resource-bounded runs of abstract machines](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-resource-bounded-runs-of-abstract-machi/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/complexity-classes/time-and-resource-bounded-runs-of-abstract-machi)
