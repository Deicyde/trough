---
declaration: section
origin: cited
lean: Cslib.Circuits.BooleanGate, Cslib.Circuits.booleanSignature, Cslib.Circuits.booleanInterpretation, Cslib.Circuits.booleanInterpretation_not, Cslib.Circuits.booleanInterpretation_and, Cslib.Circuits.booleanInterpretation_or
statement: formalized
proof: formalized
---

# Boolean circuits

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/boolean-circuits/index.html).

## Boolean gates

The Boolean gates are a NOT gate and, for each natural number $a$, an AND
gate and an OR gate indexed by $a$, which stand for gates with $a + 1$ inputs. The numbers of
inputs are assigned by the Boolean signature, so there is no AND or OR gate with zero inputs.

Formalized by `Cslib.Circuits.BooleanGate`, an inductive type declared in [CSLibExt/Computability/Circuit/Boolean.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Circuit/Boolean.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/boolean-circuits/index.html#boolean-gate).

## Boolean signature

The Boolean signature has the Boolean gates as its operation symbols,
where NOT has arity $1$ and, for each natural number $a$, the AND gate and the OR gate indexed by
$a$ have arity $a + 1$. In particular, no AND or OR gate takes zero inputs.

Formalized by `Cslib.Circuits.booleanSignature`, a definition declared in [CSLibExt/Computability/Circuit/Boolean.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Circuit/Boolean.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/boolean-circuits/index.html#boolean-signature).

## Boolean interpretation

The Boolean interpretation evaluates the gates of the Boolean
signature on the truth values $\{\mathrm{false}, \mathrm{true}\}$: NOT sends its input $x$ to
$\lnot x$, and for each natural number $a$, the AND gate and the OR gate with inputs
$x_0, \dots, x_a$ return $(\cdots((\mathrm{true} \land x_0) \land x_1) \cdots) \land x_a$ and
$(\cdots((\mathrm{false} \lor x_0) \lor x_1) \cdots) \lor x_a$ respectively, that is, the
conjunction and the disjunction of the inputs.

Formalized by `Cslib.Circuits.booleanInterpretation`, a definition declared in [CSLibExt/Computability/Circuit/Boolean.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Circuit/Boolean.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/boolean-circuits/index.html#boolean-interpretation).

## Boolean NOT

Under the Boolean interpretation, the NOT gate applied to a truth value $x$
returns its negation $\lnot x$.

Formalized by `Cslib.Circuits.booleanInterpretation_not`, a theorem declared in [CSLibExt/Computability/Circuit/Boolean.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Circuit/Boolean.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/boolean-circuits/index.html#boolean-interpretation-not).

## Boolean AND as a left fold

For every natural number $a$ and truth values
$x_0, \dots, x_a$, the Boolean interpretation of the AND gate with $a + 1$ inputs, applied to
$x_0, \dots, x_a$, returns $(\cdots((\mathrm{true} \land x_0) \land x_1) \cdots) \land x_a$,
folding conjunction over the inputs from left to right starting from true.

Formalized by `Cslib.Circuits.booleanInterpretation_and`, a theorem declared in [CSLibExt/Computability/Circuit/Boolean.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Circuit/Boolean.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/boolean-circuits/index.html#boolean-interpretation-and).

## Boolean OR as a left fold

For every natural number $a$ and truth values
$x_0, \dots, x_a$, the Boolean interpretation of the OR gate with $a + 1$ inputs, applied to
$x_0, \dots, x_a$, returns $(\cdots((\mathrm{false} \lor x_0) \lor x_1) \cdots) \lor x_a$,
folding disjunction over the inputs from left to right starting from false.

Formalized by `Cslib.Circuits.booleanInterpretation_or`, a theorem declared in [CSLibExt/Computability/Circuit/Boolean.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Circuit/Boolean.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/boolean-circuits/index.html#boolean-interpretation-or).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Boolean circuits](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/boolean-circuits/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/circuit-complexity/boolean-circuits)
