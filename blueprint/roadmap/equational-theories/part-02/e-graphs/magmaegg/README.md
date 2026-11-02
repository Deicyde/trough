# MagmaEgg

This is a simple but apparently at least somewhat effective Rust theorem prover based on egg `e-graph` library written for this project.

It proved $5574$ of the $24283$ implications in the `only_strongest.txt` file at the time.

The code was originally based on the `magma_search` pull request, but has been pretty much completely rewritten.

Currently search just uses the egg library in a basic fashion, except that in case there are extra variables not present in the LHS, it has code to instantiate them with all subexpressions of the original goal.

Exporting the proofs to Lean has turned out to be harder than finding the proofs, but a good solution has been implemented (modulo some issues in egg that require to sometimes turn off explanation optimization since it sometimes triggers stack overflows and assert failures) that directly produces proof terms using `let` / `have` and `Eq.refl`, `Eq.symm`, `Eq.trans`, `Magma.op`, a congruence lemma for `Magma.op` and variables and the hypothesis. I define one letter aliases for them to reduce verbosity.

Possible future work:

- Figure out which implications are important to prove and try it on them
- Replace the fork-based code with self-execution so that it works on Windows and is less of na hack
- Fork egg and fix the buggy and slow length optimization of explanations
- Maybe write Lean code directly instead of writing explanation sexps and converting to Lean code in a second run
- Fix the generation of extra variable values so it doesn't take too much time in pathological cases (i.e. goals with 4-6 variables)
- Determine whether it actually has some advantages compared to Vampire and `lean-egg`
- Support searching for multiple goal equations at once
- Write a custom elaborator for Lean to speed up elaboration
- If the Lean kernel turns out to be too slow for some large necessary proofs and thus the custom elaborator is not enough, write a custom verified typechecker
- Support having extra rewrite rules, such as other implications that have been found implied by the hypothesis, or simple equalities found by the egraph search itself
- Run it with massive computing resources if deemed useful and someone offers those, once it's a bit more mature
