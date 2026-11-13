---
declaration: section
origin: cited
lean: Cslib.Language.KleeneConverse.IsRegexDenoted, Cslib.Language.KleeneConverse.IsRegexDenoted.zero, Cslib.Language.KleeneConverse.IsRegexDenoted.one, Cslib.Language.KleeneConverse.IsRegexDenoted.char, Cslib.Language.KleeneConverse.IsRegexDenoted.add, Cslib.Language.KleeneConverse.IsRegexDenoted.mul, Cslib.Language.KleeneConverse.IsRegexDenoted.kstar, Cslib.Language.KleeneConverse.IsRegexDenoted.sum
statement: formalized
proof: formalized
---

# Kleene's theorem

30 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/kleene-s-theorem/index.html).

## Kleene Converse

## Language denoted by a regular expression

A language is denoted by a regular expression when it is `r.matches'` for some `r`.

Formalized by `Cslib.Language.KleeneConverse.IsRegexDenoted`, a definition declared in [CSLibExt/Computability/Languages/KleeneConverse.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/KleeneConverse.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/kleene-s-theorem/index.html#is-regex-denoted).

## The empty language is regex-denoted

The empty language is denoted by `0`.

Formalized by `Cslib.Language.KleeneConverse.IsRegexDenoted.zero`, a theorem declared in [CSLibExt/Computability/Languages/KleeneConverse.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/KleeneConverse.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/kleene-s-theorem/index.html#zero).

## The language of the empty word is regex-denoted

The language `{[]}` is denoted by `1`.

Formalized by `Cslib.Language.KleeneConverse.IsRegexDenoted.one`, a theorem declared in [CSLibExt/Computability/Languages/KleeneConverse.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/KleeneConverse.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/kleene-s-theorem/index.html#one).

## Single-letter languages are regex-denoted

A singleton `{[a]}` is denoted by `char a`.

Formalized by `Cslib.Language.KleeneConverse.IsRegexDenoted.char`, a theorem declared in [CSLibExt/Computability/Languages/KleeneConverse.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/KleeneConverse.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/kleene-s-theorem/index.html#char).

## Regex-denoted languages are closed under union

Denoted languages are closed under union.

Formalized by `Cslib.Language.KleeneConverse.IsRegexDenoted.add`, a theorem declared in [CSLibExt/Computability/Languages/KleeneConverse.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/KleeneConverse.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/kleene-s-theorem/index.html#add).

## Regex-denoted languages are closed under concatenation

Denoted languages are closed under concatenation.

Formalized by `Cslib.Language.KleeneConverse.IsRegexDenoted.mul`, a theorem declared in [CSLibExt/Computability/Languages/KleeneConverse.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/KleeneConverse.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/kleene-s-theorem/index.html#mul).

## Regex-denoted languages are closed under Kleene star

Denoted languages are closed under Kleene star.

Formalized by `Cslib.Language.KleeneConverse.IsRegexDenoted.kstar`, a theorem declared in [CSLibExt/Computability/Languages/KleeneConverse.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/KleeneConverse.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/kleene-s-theorem/index.html#kstar).

## Regex-denoted languages are closed under finite unions

Denoted languages are closed under finite unions.

Formalized by `Cslib.Language.KleeneConverse.IsRegexDenoted.sum`, a theorem declared in [CSLibExt/Computability/Languages/KleeneConverse.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/KleeneConverse.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/kleene-s-theorem/index.html#sum).

## Membership in a finite union of languages

Membership in a finite union of languages.

Formalized by `Cslib.Language.KleeneConverse.mem_sum`, a theorem declared in [CSLibExt/Computability/Languages/KleeneConverse.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/KleeneConverse.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/kleene-s-theorem/index.html#mem-sum).

## Empty word outside a concatenation

The empty word is not in a concatenation whose right factor excludes it.

Formalized by `Cslib.Language.KleeneConverse.nil_notMem_mul_of_nil_notMem_right`, a theorem declared in [CSLibExt/Computability/Languages/KleeneConverse.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/KleeneConverse.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/kleene-s-theorem/index.html#nil-not-mem-mul-of-nil-not-mem-right).

## Coefficient in the equation system of a DFA

The system of equations of a DFA at a state: the coefficient of `X j` in the
equation for `X q`, the finite union of the singletons `{[a]}` over the letters taking
`q` to `j`.

Formalized by `Cslib.Language.KleeneConverse.coeff`, a definition declared in [CSLibExt/Computability/Languages/KleeneConverse.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/KleeneConverse.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/kleene-s-theorem/index.html#coeff).

## Constant term in the equation system of a DFA

The constant term of the equation for `X q`: `1` on accepting states, `0` otherwise.

Formalized by `Cslib.Language.KleeneConverse.constTerm`, a definition declared in [CSLibExt/Computability/Languages/KleeneConverse.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/KleeneConverse.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/kleene-s-theorem/index.html#const-term).

## Language accepted from a DFA state

The language accepted from a state: the unknown `X q` of the system.

Formalized by `Cslib.Language.KleeneConverse.fromState`, a definition declared in [CSLibExt/Computability/Languages/KleeneConverse.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/KleeneConverse.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/kleene-s-theorem/index.html#from-state).

## Membership in a DFA equation coefficient

Membership in a coefficient: the word is a single letter taking `q` to `j`.

Formalized by `Cslib.Language.KleeneConverse.mem_coeff`, a theorem declared in [CSLibExt/Computability/Languages/KleeneConverse.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/KleeneConverse.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/kleene-s-theorem/index.html#mem-coeff).

## DFA equation coefficients exclude the empty word

No coefficient contains the empty word.

Formalized by `Cslib.Language.KleeneConverse.nil_notMem_coeff`, a theorem declared in [CSLibExt/Computability/Languages/KleeneConverse.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/KleeneConverse.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/kleene-s-theorem/index.html#nil-not-mem-coeff).

## DFA equation coefficients are regex-denoted

Every coefficient is denoted by a regular expression.

Formalized by `Cslib.Language.KleeneConverse.denoted_coeff`, a theorem declared in [CSLibExt/Computability/Languages/KleeneConverse.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/KleeneConverse.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/kleene-s-theorem/index.html#denoted-coeff).

## DFA equation constant terms are regex-denoted

Every constant term is denoted by a regular expression.

Formalized by `Cslib.Language.KleeneConverse.denoted_constTerm`, a theorem declared in [CSLibExt/Computability/Languages/KleeneConverse.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/KleeneConverse.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/kleene-s-theorem/index.html#denoted-const-term).

## Equation system satisfied by DFA state languages

The DFA equations: from `q`, either step on a letter and continue, or stop if `q`
accepts.

Formalized by `Cslib.Language.KleeneConverse.fromState_eq`, a theorem declared in [CSLibExt/Computability/Languages/KleeneConverse.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/KleeneConverse.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/kleene-s-theorem/index.html#from-state-eq).

## Coefficient after eliminating the last state

The coefficient of the reduced system obtained by eliminating the last state: the old
coefficient, plus the detour through the last state, which may loop there any number of
times.

Formalized by `Cslib.Language.KleeneConverse.elimCoeff`, a definition declared in [CSLibExt/Computability/Languages/KleeneConverse.lean, line 235](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/KleeneConverse.lean#L235). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/kleene-s-theorem/index.html#elim-coeff).

## Constant term after eliminating the last state

The constant term of the reduced system obtained by eliminating the last state.

Formalized by `Cslib.Language.KleeneConverse.elimConst`, a definition declared in [CSLibExt/Computability/Languages/KleeneConverse.lean, line 243](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/KleeneConverse.lean#L243). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/kleene-s-theorem/index.html#elim-const).

## Solving a system of language equations

If the languages `X i` satisfy
`X i = (∑ j, A i j * X j) + B i` with every coefficient `A i j` excluding the empty word
and every coefficient and constant term denoted by a regular expression, then every `X i`
is denoted by a regular expression. The proof eliminates the last state with Arden's lemma
and applies the induction hypothesis to the reduced system.

Formalized by `Cslib.Language.KleeneConverse.exists_regex_of_system`, a theorem declared in [CSLibExt/Computability/Languages/KleeneConverse.lean, line 254](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/KleeneConverse.lean#L254). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/kleene-s-theorem/index.html#exists-regex-of-system).

## Languages of DFAs on finitely many numbered states are regex-denoted

The language of a DFA with `Fin n` states is denoted by a regular expression.

Formalized by `Cslib.Language.KleeneConverse.exists_regex_of_dfa_fin`, a theorem declared in [CSLibExt/Computability/Languages/KleeneConverse.lean, line 334](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/KleeneConverse.lean#L334). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/kleene-s-theorem/index.html#exists-regex-of-dfa-fin).

## Kleene's theorem: DFA languages are regex-denoted

The language of a DFA over a finite state type is denoted by a regular expression.

Formalized by `Cslib.Language.KleeneConverse.exists_regex_of_dfa`, a theorem declared in [CSLibExt/Computability/Languages/KleeneConverse.lean, line 345](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/KleeneConverse.lean#L345). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/kleene-s-theorem/index.html#exists-regex-of-dfa).

## Letters occurring in a regular expression

The letters occurring in a regular expression.

Formalized by `Cslib.Language.KleeneConverse.regexLetters`, a definition declared in [CSLibExt/Computability/Languages/KleeneConverse.lean, line 353](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/KleeneConverse.lean#L353). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/kleene-s-theorem/index.html#regex-letters).

## Letters of matched words occur in the regular expression

Every letter of a word matched by `r` occurs in `r`.

Formalized by `Cslib.Language.KleeneConverse.mem_matches'_letters`, a theorem declared in [CSLibExt/Computability/Languages/KleeneConverse.lean, line 362](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/KleeneConverse.lean#L362). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/kleene-s-theorem/index.html#mem-matches-letters).

## DFA accepting the one-letter words

The three-state DFA accepting exactly the one-letter words.

Formalized by `Cslib.Language.KleeneConverse.singletonDFA`, a definition declared in [CSLibExt/Computability/Languages/KleeneConverse.lean, line 390](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/KleeneConverse.lean#L390). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/kleene-s-theorem/index.html#singleton-dfa).

## The one-letter-word DFA accepts exactly words of length one

The one-letter-word DFA accepts exactly the words of length one.

Formalized by `Cslib.Language.KleeneConverse.singletonDFA_accepts`, a theorem declared in [CSLibExt/Computability/Languages/KleeneConverse.lean, line 396](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/KleeneConverse.lean#L396). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/kleene-s-theorem/index.html#singleton-dfa-accepts).

## Kleene's theorem, converse direction

**Kleene's theorem, converse direction** (Sipser, *Introduction to the Theory of
Computation*, 3rd ed., Theorem 1.54): every regular language over a finite alphabet is denoted
by a regular expression. Source: M. Sipser, *Introduction to the Theory of Computation*, 3rd
ed., Theorem 1.54.

Formalized by `Cslib.Language.IsRegular.exists_regex`, a theorem declared in [CSLibExt/Computability/Languages/KleeneConverse.lean, line 455](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/KleeneConverse.lean#L455). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/kleene-s-theorem/index.html#exists-regex).

## Kleene's theorem

**Kleene's theorem** (Sipser, 3rd ed., Theorem 1.54): over a finite alphabet, a language
is regular if and only if it is denoted by a regular expression. Source: M. Sipser,
*Introduction to the Theory of Computation*, 3rd ed., Theorem 1.54.

Formalized by `Cslib.Language.isRegular_iff_exists_regex`, a theorem declared in [CSLibExt/Computability/Languages/KleeneConverse.lean, line 464](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/KleeneConverse.lean#L464). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/kleene-s-theorem/index.html#is-regular-iff-exists-regex).

## Sharpness of the finite-alphabet hypothesis

Over an infinite alphabet, the language
of one-letter words is regular but is denoted by no regular expression, since a regular
expression mentions only finitely many letters. Source: M. Sipser, *Introduction to the
Theory of Computation*, 3rd ed., Theorem 1.54 (finite alphabet).

Formalized by `Cslib.Language.exists_regular_not_regex`, a theorem declared in [CSLibExt/Computability/Languages/KleeneConverse.lean, line 472](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/KleeneConverse.lean#L472). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/kleene-s-theorem/index.html#exists-regular-not-regex).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Kleene's theorem](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/kleene-s-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/kleene-s-theorem)
