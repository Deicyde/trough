from trough import leansource

SOURCE = '''/-
Copyright: theorem inHeader : True
-/
module

public import Mathlib.Order.Basic

/-! # A module docstring naming `theorem inModuleDoc` -/

@[expose] public section

theorem A.b : True := trivial

namespace A

/-- A docstring: `theorem inDocstring : True := trivial`. -/
@[simp,
  reducible]
lemma c : True := by
  trivial

-- theorem inLineComment : True
/- nested /- theorem inNested -/ theorem stillInComment -/

def quote : String := "theorem inString : True"
def quoteChar : Char := '"'
def afterChar : Nat := 1

theorem _root_.Top.level : True := trivial

open Classical in theorem opened : True := trivial

instance : Inhabited Nat := ⟨0⟩
instance (priority := 100) named : Inhabited Nat := ⟨1⟩
private theorem hidden : True := trivial
def universes.{u} (α : Sort u) : Sort u := α

namespace B.C

theorem stated : True := by
  sorry

theorem proved : True := by
  exact trivial
example : True := sorry

end B.C

noncomputable section Named

protected theorem inSection : True := trivial

end Named

end A
'''


def test_the_scan_follows_namespaces_sections_and_root():
    found = leansource.scan(SOURCE)
    assert found is not None
    assert set(found) == {"A.b", "A.c", "A.quote", "A.quoteChar", "A.afterChar", "Top.level", "A.opened", "A.named",
                          "A.universes", "A.B.C.stated", "A.B.C.proved", "A.inSection"}
    assert found["A.b"].line == 12 and found["A.b"].kind == "theorem"
    assert found["A.c"].kind == "lemma" and found["A.c"].line == 19
    assert found["A.named"].kind == "instance"


def test_names_in_comments_docstrings_and_strings_are_not_declarations():
    found = leansource.scan(SOURCE)
    for name in ("inHeader", "inModuleDoc", "inDocstring", "inLineComment", "inNested", "stillInComment", "inString"):
        assert not any(full.endswith(name) for full in found)


def test_a_declaration_whose_text_holds_sorry_is_flagged_and_the_next_is_not():
    found = leansource.scan(SOURCE)
    assert found["A.B.C.stated"].sorry
    # The example after it holds a sorry too, but it is a command of its own.
    assert not found["A.B.C.proved"].sorry
    assert not found["A.c"].sorry


def test_scopes_that_do_not_close_as_they_open_declare_nothing():
    assert leansource.scan("namespace A\ntheorem x : True := trivial\nend B\n") is None
    assert leansource.scan("namespace A\nend\n") is None
    assert leansource.scan("end A\n") is None
    # A scope left open at the end of the file is fine, as in Lean.
    assert set(leansource.scan("namespace A\nsection\ntheorem x : True := trivial\n")) == {"A.x"}
    # `end A.B` closes namespaces A and B opened one at a time.
    assert set(leansource.scan("namespace A\nnamespace B\ntheorem x : True := trivial\nend A.B\ntheorem y : True := trivial\n")) == {
        "A.B.x", "y"}


def test_a_name_on_the_line_after_its_keyword_is_not_read():
    assert leansource.scan("theorem\n  late : True := trivial\n") == {}


def test_is_name_accepts_one_lean_name_only():
    assert leansource.is_name("AdicCompletion.map_exact_of_isNoetherian_middle")
    assert leansource.is_name("Nat.succ_le'")
    assert leansource.is_name("«term_∘_»")
    assert not leansource.is_name("A.b, A.c")
    assert not leansource.is_name("f : X → Y")
    assert not leansource.is_name("Order.height_pi and Order.coheight_pi")
    assert not leansource.is_name(".b")


def test_a_private_declaration_is_not_declared():
    # Lean names it `_private...`, so no one can refer to it by the name it is written with.
    assert "A.hidden" not in leansource.scan(SOURCE)


def test_mutual_blocks_and_named_sections_close():
    text = ("namespace A\nmutual\ntheorem even : True := trivial\ntheorem odd : True := trivial\nend\n"
            "section B.C\ntheorem inner : True := trivial\nend B.C\nend A\ntheorem after : True := trivial\n")
    assert set(leansource.scan(text)) == {"A.even", "A.odd", "A.inner", "after"}
    # A section named with a dot closes at the top level too.
    assert set(leansource.scan("section A.B\ntheorem x : True := trivial\nend A.B\n")) == {"x"}


def test_nothing_after_exit_is_read():
    text = "theorem kept : True := by\n  trivial\n#exit\ntheorem dropped : True := sorry\n"
    found = leansource.scan(text)
    assert set(found) == {"kept"} and not found["kept"].sorry


def test_sorry_ax_and_stop_count_as_sorry():
    text = ("theorem ax : True := sorryAx True\ntheorem stopped : True := by\n  stop\n  trivial\n"
            "theorem fine : True := by\n  exact trivial\n"
            "def config : Config where\n  stop := 5\n  start := 0\n")
    found = leansource.scan(text)
    assert found["ax"].sorry and found["stopped"].sorry and not found["fine"].sorry
    # A field named `stop` is not the tactic.
    assert not found["config"].sorry


def test_a_docstring_opened_by_slash_dash_dash_slash_runs_to_its_close():
    text = "/--/ theorem inDoc : True := trivial -/\ntheorem real : True := trivial\n"
    assert set(leansource.scan(text)) == {"real"}


def test_raw_strings_have_no_escapes():
    text = ('def a : String := r"\\"\ntheorem afterRaw : True := trivial\n'
            'def b : String := r#"a "quoted" theorem inRaw : True"#\ntheorem afterHashes : True := trivial\n')
    assert set(leansource.scan(text)) == {"a", "afterRaw", "b", "afterHashes"}


def test_an_alias_is_a_declaration_and_an_anonymous_instance_is_not_named():
    text = ("namespace A\ntheorem long_name : True := trivial\n/-- Short. -/\nalias short := long_name\n"
            "alias ⟨mp, mpr⟩ := Iff.rfl\ninstance : Inhabited Nat := ⟨0⟩\nend A\n")
    found = leansource.scan(text)
    assert set(found) == {"A.long_name", "A.short"} and found["A.short"].kind == "alias"


def test_an_indented_end_inside_a_declaration_is_part_of_it():
    # A notation may use the word, as an assembly program's `begin ... end` does.
    text = ("namespace A\ntheorem prog : hoare\n  begin\n    li x 1, 0\n  end\n  := by\n  trivial\n\n"
            "theorem after : True := trivial\nend A\n")
    assert set(leansource.scan(text)) == {"A.prog", "A.after"}
    # Indented, with no declaration open, it still closes its scope.
    assert set(leansource.scan("namespace A\n  end A\ntheorem top : True := trivial\n")) == {"top"}


ATTACHED = '''/-!
# A problem

*Reference:* [example.org/1](https://example.org/1)
-/

namespace P

/-- Not this one's: a docstring for `helper`. -/
def helper : ℕ := 0

set_option linter.style.formal_proof_palomar false in
/--
The main statement,
  indented.
-/
@[category research solved, AMS 5 11, -- a comment, ignored
  formal_proof using lean4 at
    "https://example.org/a,b"]
theorem main (n : ℕ := 0) : let m := n; m = n := by
  sorry

@[simp] theorem inline : True := trivial

/-- Its value holds no `sorry`, though its statement does. -/
@[category test]
theorem answered : (sorry : ℕ) = sorry := rfl

theorem byFields : True ∧ True where
  left := trivial
  right := sorry

/-- A docstring with no attributes. -/
theorem plain : True :=
  trivial

def byCases : ℕ → ℕ
  | 0 => 0
  | n + 1 => n

end P
'''


def test_a_declaration_carries_its_docstring_and_attribute_list():
    found = leansource.scan(ATTACHED)
    main = found["P.main"]
    assert main.doc == "The main statement,\n  indented."
    assert main.attributes == ("category research solved", "AMS 5 11",
                               'formal_proof using lean4 at "https://example.org/a,b"')
    assert found["P.inline"].attributes == ("simp",) and found["P.inline"].doc == ""
    assert found["P.plain"].doc == "A docstring with no attributes." and found["P.plain"].attributes == ()
    assert found["P.helper"].doc == "Not this one's: a docstring for `helper`." and found["P.helper"].attributes == ()


def test_a_statement_runs_to_the_value_and_sorry_is_read_in_the_value():
    found = leansource.scan(ATTACHED)
    # A default argument's `:=` sits in brackets, and a `let` claims the next one.
    assert found["P.main"].statement == "theorem main (n : ℕ := 0) : let m := n; m = n"
    assert found["P.main"].sorry and found["P.main"].proof_sorry
    assert found["P.answered"].statement == "theorem answered : (sorry : ℕ) = sorry"
    assert found["P.answered"].sorry and not found["P.answered"].proof_sorry
    assert found["P.byFields"].statement == "theorem byFields : True ∧ True" and found["P.byFields"].proof_sorry
    assert found["P.plain"].statement == "theorem plain : True" and not found["P.plain"].proof_sorry
    # A definition by pattern matching has no `:=` to end its statement.
    assert found["P.byCases"].statement is None and not found["P.byCases"].proof_sorry


def test_the_module_docstring_is_the_first_one():
    assert leansource.module_doc(ATTACHED) == "# A problem\n\n*Reference:* [example.org/1](https://example.org/1)"
    assert leansource.module_doc("theorem x : True := trivial\n") is None


def test_attribute_lists_split_at_top_level_commas_only():
    assert leansource.split_attributes(' simp, foo [a, b],\n  bar "x, y" ') == ["simp", "foo [a, b]", 'bar "x, y"']


EXAMPLES = '''namespace E

/-- Example 1.2: a documented example. -/
example : 1 + 1 = 2 := by
  sorry

theorem named : True := trivial
open Nat in example (n : ℕ) : n + 0 = n := by
  simp

section
  example : True := trivial
  end

/-- Exercise 1.3 -/
example : (sorry : Prop) := by sorry

end E

example : True where
'''


def test_scan_with_examples_adds_the_examples_and_keeps_the_declarations():
    for text in (SOURCE, ATTACHED, EXAMPLES):
        found, _ = leansource.scan_with_examples(text)
        assert found == leansource.scan(text)
    found, examples = leansource.scan_with_examples(EXAMPLES)
    assert set(found) == {"E.named"}
    assert [(example.line, example.kind, example.name) for example in examples] == [
        (4, "example", ""), (8, "example", ""), (16, "example", ""), (20, "example", "")]
    first, opened, exercise, last = examples
    assert first.doc == "Example 1.2: a documented example." and first.statement == "example : 1 + 1 = 2"
    assert first.proof_sorry
    # An `open ... in` prefix is not part of the statement, as for a declaration.
    assert opened.statement == "example (n : ℕ) : n + 0 = n" and not opened.proof_sorry and opened.doc == ""
    assert exercise.statement == "example : (sorry : Prop)" and exercise.proof_sorry
    assert last.statement == "example : True"
    # The indented example and its indented `end` are read as scan() reads them: the example is not one, and
    # the `end` closes the section.
    assert leansource.scan_with_examples("example : True := by\n  end\n") is None
    assert leansource.scan_with_examples("theorem t : True := by\n  end\n") == ({"t": leansource.scan(
        "theorem t : True := by\n  end\n")["t"]}, [])
