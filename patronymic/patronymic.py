def generate_patronymic(name: str, gender: str) -> str:
    if gender not in {"male", "female"}:
        raise ValueError("Gender must be 'male' or 'female'.")

    # 0. Fucking Павел
    if name.endswith('ел'):
        return name[:-2] + ("лович" if gender == "male" else "ловна")

    # 1. Ends in a hard consonant (except ж, ш, ч, щ, ц → ович / овна) and р - see next
    if name[-1] in "бвгджзклмнпстфх":
        return name + ("ович" if gender == "male" else "овна")

    # 2. Ends in an р - fucking Пётр exception
    if name[-1] == 'р':
        return name.replace('ё', 'е') + ("ович" if gender == "male" else "овна")

    # 3. Ends in ж, ш, ч, щ, ц → евич / евна
    if name[-1] in "жшчщц":
        return name + ("евич" if gender == "male" else "евна")

    # 4. Ends in unstressed а, у, ы → drop vowel, add ович / овна
    if name[-1] in "ауы" and name[-2] not in "жшчщц":
        return name[:-1] + ("ович" if gender == "male" else "овна")

    # Exception: Traditional forms like Никита → Никитич / Никитична
    if name in {"Аникита", "Никита", "Мина", "Савва", "Сила", "Фока"}:
        return name[:-1] + ("ич" if gender == "male" else "ична")

    # 5. Ends in unstressed о → drop о, add ович / овна
    if name[-1] == "о":
        return name[:-1] + ("ович" if gender == "male" else "овна")

    # 6. Ends in unstressed vowel preceded by ж, ш, ч, щ, ц → евич / евна
    if len(name) > 1 and name[-2] in "жшчщц" and name[-1] in "аеуыо":
        return name[:-1] + ("евич" if gender == "male" else "евна")

    # 7. Ends in soft consonant (ь) → drop ь, add евич / евна
    if name[-1] == "ь":
        return name[:-1] + ("евич" if gender == "male" else "евна")

    # 8. Ends in unstressed е → merge with евич / евна
    if name[-1] == "е":
        return name[:-1] + ("евич" if gender == "male" else "евна")

    # 9. Ends in unstressed и → keep и, add евич / евна
    if name[-1] == "и":
        return name + ("евич" if gender == "male" else "евна")

    # 10. Ends in unstressed ий → drop й, handle special cases
    if name.endswith("ий"):
        if name.endswith("лий") or name.endswith("рий"):  # Савелий → Савельевич, Юрий - Юрьевна
            return name[:-2] + ("ьевич" if gender == "male" else "ьевна")
        if len(name) > 2 and name[-3] in "нт":  # Василий → Васильевич
            return name[:-2] + ("ьевич" if gender == "male" else "ьевна")
        return name[:-2] + ("иевич" if gender == "male" else "иевна")

    # 11. Ends in ея / ия → drop я, add евич / евна
    if name.endswith(("ея", "ия")):
        return name[:-1] + ("евич" if gender == "male" else "евна")

    # 12. Ends in stressed vowel → keep vowel, add евич / евна
    if name[-1] in "аяеэиыёоую":
        return name + ("евич" if gender == "male" else "евна")

    # 13. Ends in stressed ай, яй, ей, эй, ий, ый, ой, уй, юй → drop й, add евич / евна
    if name[-2:] in {"ай", "яй", "ей", "эй", "ий", "ый", "ой", "уй", "юй"}:
        return name[:-1] + ("евич" if gender == "male" else "евна")

    # 14. Ends in double vowel аа, ау, еу, ээ, ии, уу → keep vowels, add евич / евна
    if len(name) > 1 and name[-2:] in {"аа", "ау", "еу", "ээ", "ии", "уу"}:
        return name + ("евич" if gender == "male" else "евна")

    # Default fallback
    return name + ("ович" if gender == "male" else "овна")

